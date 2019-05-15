from interface.Matrix import MatrixInterface
from enumTypes.EnterMatrixStates import EnterStates
from enumTypes.LootsTypes import LootsTypes
from exceptions.ErrorValue import ErrorValue


class EnterInterface(MatrixInterface):
    def __init__(self):
        super().__init__()

    def create_matrix(self, text, enter_type):
        self._type_of_numbers = LootsTypes.INTEGER
        text = text.strip()

        if text.find(".") != -1:
            self._type_of_numbers = LootsTypes.REAL

        lines = text.splitlines()

        for index in range(len(lines)):
            lines[index] = lines[index].strip().split()

        try:
            matrix = [[int(lines[i][j]) if self._type_of_numbers == LootsTypes.INTEGER else float(lines[i][j])
                       for j in range(len(lines[i]))] for i in range(len(lines))]
        except ValueError:
            raise ErrorValue("Incorrect values ​​provided!")
        except Exception:
            raise ErrorValue("Unknown error!")

        if len(matrix) < 1:
            raise ErrorValue("Incorrect size of the matrix!")

        if enter_type == EnterStates.FIRST:
            self._first_row = len(lines)
            if self._first_row < 1:
                raise ErrorValue("Incorrect size of the matrix!")
            self._first_column = len(lines[0])
        elif enter_type == EnterStates.SECOND:
            self._second_row = len(lines)
            if self._second_row < 1:
                raise ErrorValue("Incorrect size of the matrix!")
            self._second_column = len(lines[0])

        for row in matrix:
            if enter_type == EnterStates.FIRST and len(row) != self._first_column:
                raise ErrorValue("The matrix columns have different sizes!")
            elif enter_type == EnterStates.SECOND and len(row) != self._second_column:
                raise ErrorValue("The matrix columns have different sizes!")

        if enter_type == EnterStates.SECOND and self._first_column != self._second_row:
            raise ErrorValue("Number of columns in 1 matrix must be equal to rows in 2!")

        if enter_type == EnterStates.FIRST:
            self._matrix_one = matrix
        elif enter_type == EnterStates.SECOND:
            self._matrix_two = matrix

        return matrix

