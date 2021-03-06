#include "stdafx.h"
#include "MultiplicationDLL.h"

double** multiplicationDouble(double **matrix_one, double **matrix_two, int matrix_column_one, int matrix_row_one, int matrix_column_two, int matrix_row_two) {
	return multiplicationT<double>(matrix_one, matrix_two, matrix_column_one, matrix_row_one, matrix_column_two, matrix_row_two);
};
int** multiplicationInt(int **matrix_one, int **matrix_two, int matrix_column_one, int matrix_row_one, int matrix_column_two, int matrix_row_two) {
	return multiplicationT<int>(matrix_one, matrix_two, matrix_column_one, matrix_row_one, matrix_column_two, matrix_row_two);
};
