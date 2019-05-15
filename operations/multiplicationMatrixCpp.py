from operations.multiplicationMatrix import MultiplicationMatrix
from enumTypes.LootsTypes import LootsTypes
from enumTypes.EnterMatrixStates import EnterStates
from ctypes import c_double, c_int, cdll, POINTER
from os import path


class MultiplicationMatrixCpp(MultiplicationMatrix):
    def __init__(self, matrix_one, matrix_two, iterations, numbers_type):
        super().__init__(matrix_one, matrix_two, iterations, numbers_type)
        self._c_numbers_type = None
        self._c_function = None
        self.c_matrix_one = None
        self._c_matrix_two = None

        c_lib = cdll.LoadLibrary(path.join(path.dirname(__file__), './../dlls/MultiplicationDLL.dll'))

        if self._numbers_type == LootsTypes.INTEGER:
            self._c_function = c_lib["multiplicationInt"]
        else:
            self._c_function = c_lib["multiplicationDouble"]

        self._row_one = len(matrix_one)
        self._column_one = len(matrix_one[0])
        self._row_two = self._column_one
        self._column_two = len(matrix_two[0])

    @MultiplicationMatrix.calculate_time
    def prepare_data(self):
        for _ in range(self._iterations):
            if self._numbers_type == LootsTypes.INTEGER:
                self._c_numbers_type = c_int
            else:
                self._c_numbers_type = c_double

            ptr_ptr_c_number_type = POINTER(POINTER(self._c_numbers_type))
            self._c_function.argtypes = (ptr_ptr_c_number_type, ptr_ptr_c_number_type, c_int, c_int, c_int, c_int)
            self._c_function.restype = ptr_ptr_c_number_type

            self.c_matrix_one = self._create_cpp_matrix(EnterStates.FIRST)
            self._c_matrix_two = self._create_cpp_matrix(EnterStates.SECOND)

    def _create_cpp_matrix(self, matrix_type):
        if matrix_type == EnterStates.FIRST:
            row = self._row_one
            column = self._column_one
            matrix = self._matrix_one
        else:
            row = self._row_two
            column = self._column_two
            matrix = self._matrix_two

        c_matrix_scheme = POINTER(self._c_numbers_type) * row
        c_column_scheme = self._c_numbers_type * column

        c_matrix = c_matrix_scheme()
        for i in range(row):
            c_matrix[i] = c_column_scheme()
            for j in range(column):
                c_matrix[i][j] = matrix[i][j]

        return c_matrix

    @MultiplicationMatrix.calculate_time
    def multiplication(self):
        result_matrix = None
        for _ in range(self._iterations):
            result_matrix = self._c_function(self.c_matrix_one, self._c_matrix_two, c_int(self._column_one), c_int(self._row_one), c_int(self._column_two), c_int(self._row_two))

        return result_matrix
