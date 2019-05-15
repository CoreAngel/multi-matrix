from time import time


class MultiplicationMatrix:
    def __init__(self, matrix_one, matrix_two, iterations, numbers_type):
        self._matrix_one = matrix_one
        self._matrix_two = matrix_two
        self._iterations = iterations
        self._numbers_type = numbers_type

    def multiplication(self):
        pass

    def calculate_time(function):
        def inner(*args, **kwargs):
            start = time()
            result = function(*args, **kwargs)
            finish = time()

            passed = finish - start
            return result, passed

        return inner

