from operations.multiplicationMatrixPython import MultiplicationMatrixPython
from operations.multiplicationMatrixCpp import MultiplicationMatrixCpp
from enumTypes.LootsTypes import LootsTypes
from exceptions.ErrorValue import ErrorValue


class MatrixInterface:
    def __init__(self):
        self._matrix_one = None
        self._matrix_two = None

        self._first_column = None
        self._first_row = None
        self._second_column = None
        self._second_row = None
        self._iterations = None
        self._type_of_numbers = None

        self._result_matrix_py = None
        self._result_matrix_cpp = None

        self._time_py = None
        self._time_cpp = None
        self._time_conv = None

    def check_iteration(self, iterations, type_of_numbers=None):

        if type_of_numbers is not None:
            if type_of_numbers == str(LootsTypes.INTEGER):
                self._type_of_numbers = LootsTypes.INTEGER
            else:
                self._type_of_numbers = LootsTypes.REAL

        try:
            self._iterations = int(iterations)
        except ValueError:
            raise ErrorValue("Podana ilosc iteracji jest niepoprawna")
        except Exception:
            raise ErrorValue("Wystapil nieznany blad")

        if self._iterations < 1:
            raise ErrorValue("Ilosc iteracji nie moze byc mniejsza niz 1")

    def calculate(self):
        multi_python = MultiplicationMatrixPython(self._matrix_one, self._matrix_two, self._iterations, self._type_of_numbers)
        multi_cpp = MultiplicationMatrixCpp(self._matrix_one, self._matrix_two, self._iterations, self._type_of_numbers)
        _, self._time_conv = multi_cpp.prepare_data()
        self._result_matrix_py, self._time_py = multi_python.multiplication()
        result_matrix_cpp, self._time_cpp = multi_cpp.multiplication()

        self._result_matrix_cpp = [[result_matrix_cpp[i][j] for j in range(self._second_column)] for i in
                                   range(self._first_row)]

    def get_result_matrix_py(self):
        return self._result_matrix_py

    def get_result_matrix_cpp(self):
        return self._result_matrix_cpp

    def get_time_py(self):
        return self._time_py

    def get_time_cpp(self):
        return self._time_cpp

    def get_time_conv(self):
        return self._time_conv


