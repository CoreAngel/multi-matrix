from operations.multiplicationMatrix import MultiplicationMatrix


class MultiplicationMatrixPython(MultiplicationMatrix):
    def __init__(self, matrix_one, matrix_two, iterations, numbers_type):
        super().__init__(matrix_one, matrix_two, iterations, numbers_type)

    @MultiplicationMatrix.calculate_time
    def multiplication(self):
        result_matrix = None
        for _ in range(self._iterations):
            result_matrix = [[sum(a * b for a, b in zip(matrix_one_row, matrix_two_col))
                              for matrix_two_col in zip(*self._matrix_two)] for matrix_one_row in self._matrix_one]

        return result_matrix

