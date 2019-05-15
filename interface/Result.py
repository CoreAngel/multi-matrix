from enumTypes.ResultMatrixTypes import ResultMatrixTypes
from enumTypes.ResultTimeTypes import ResultTimeTypes


class ResultInterface:
    def __init__(self):
        self._calculation = False

        self._time_python = None
        self._time_cpp = None
        self._time_conversion = None

        self._matrix_one = None
        self._matrix_two = None
        self._result_py = None
        self._result_cpp = None

    def set_matrix(self, matrix, matrix_type):
        if matrix_type == ResultMatrixTypes.FIRST:
            self._matrix_one = matrix
        elif matrix_type == ResultMatrixTypes.SECOND:
            self._matrix_two = matrix
        elif matrix_type == ResultMatrixTypes.RESULT_PY:
            self._result_py = matrix
        elif matrix_type == ResultMatrixTypes.RESULT_CPP:
            self._result_cpp = matrix

    def get_matrix(self, matrix_type):
        if matrix_type == ResultMatrixTypes.FIRST:
            return self._matrix_one
        elif matrix_type == ResultMatrixTypes.SECOND:
            return self._matrix_two
        elif matrix_type == ResultMatrixTypes.RESULT_PY:
            return self._result_py
        elif matrix_type == ResultMatrixTypes.RESULT_CPP:
            return self._result_cpp
        else:
            return None

    def set_time(self, time, time_type):
        if time_type == ResultTimeTypes.PYTHON:
            self._time_python = time
        elif time_type == ResultTimeTypes.CPP:
            self._time_cpp = time
        elif time_type == ResultTimeTypes.CONVERSION:
            self._time_conversion = time

    def get_time(self, time_type):
        if time_type == ResultTimeTypes.PYTHON:
            return self._time_python
        elif time_type == ResultTimeTypes.CPP:
            return self._time_cpp
        elif time_type == ResultTimeTypes.CONVERSION:
            return self._time_conversion
        else:
            return None

    def set_calculation_status(self, value):
        self._calculation = bool(value)

    def get_calculation_status(self):
        return self._calculation

    def reset_matrixs(self):
        self._matrix_one = None
        self._matrix_two = None
        self._result_py = None
        self._result_cpp = None

