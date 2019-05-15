from interface.Matrix import MatrixInterface
from enumTypes.LootsTypes import LootsTypes
from exceptions.ErrorValue import ErrorValue
from math import floor, ceil
from random import uniform


class RandomInterface(MatrixInterface):
    def __init__(self):
        super().__init__()

        self._interval_from = None
        self._interval_to = None

    def check_size(self, first_matrix, second_matrix):
        try:
            (first_row, first_column) = first_matrix.strip().split()
            (second_row, second_column) = second_matrix.strip().split()
            self._first_column = int(first_column)
            self._first_row = int(first_row)
            self._second_column = int(second_column)
            self._second_row = int(second_row)
        except ValueError:
            raise ErrorValue("Podane wielkości macierzy są niepoprawne")
        except Exception:
            raise Exception("Wystapil nieznany blad")

        if self._first_column < 1 or self._first_row < 1 or self._second_column < 1 or self._second_row < 1:
            raise ErrorValue("Wielkosc macierzy nie moze byc mniejsza niz 1")

        if self._first_column != self._second_row:
            raise ErrorValue("Ilosc kolumn w 1 macierzy musi byc rowna ilosci wierszy w 2")

    def check_interval(self, interval_from, interval_to):
        try:
            self._interval_from = float(interval_from)
            self._interval_to = float(interval_to)
        except ValueError:
            raise ErrorValue("Podane wartosci sa niepoprawne")
        except Exception:
            raise Exception("Wystapil nieznany blad")

        if self._interval_from > self._interval_to:
            raise ErrorValue("Podano niepoprawny przedział")

        if self._type_of_numbers == LootsTypes.INTEGER:
            self._interval_from = ceil(self._interval_from)
            self._interval_to = floor(self._interval_to)

    def create_matrix_one(self):
        self._matrix_one = [[uniform(self._interval_from, self._interval_to)
                            if self._type_of_numbers == LootsTypes.REAL
                            else round(uniform(self._interval_from, self._interval_to))
                             for _ in range(self._first_column)] for _ in range(self._first_row)]
        return self._matrix_one

    def create_matrix_two(self):
        self._matrix_two = [[uniform(self._interval_from, self._interval_to)
                            if self._type_of_numbers == LootsTypes.REAL
                            else round(uniform(self._interval_from, self._interval_to))
                             for _ in range(self._second_column)] for _ in range(self._second_row)]
        return self._matrix_two

