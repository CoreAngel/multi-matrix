#pragma once

#ifdef MULTIPLICATIONDLL_EXPORTS
#define DLLDIR  __declspec(dllexport)   // export DLL information
#else
#define DLLDIR  __declspec(dllimport)   // import DLL information
#endif 

template<class T>
T** multiplicationT(T **matrix_one, T **matrix_two, int matrix_column_one, int matrix_row_one, int matrix_column_two, int matrix_row_two) {

	T** result_matrix = new T*[matrix_row_one];
	for (int i = 0; i < matrix_row_one; ++i) {
		result_matrix[i] = new T[matrix_column_two];
		for (int j = 0; j < matrix_column_two; ++j) {
			result_matrix[i][j] = 0;
		}
	}

	for (int i = 0; i<matrix_row_one; ++i) {
		for (int j = 0; j<matrix_column_two; ++j) {
			for (int k = 0; k<matrix_column_one; ++k)
			{
				result_matrix[i][j] += matrix_one[i][k] * matrix_two[k][j];
			}
		}
	}
	return result_matrix;
};
extern "C" {
	DLLDIR double** multiplicationDouble(double **matrix_one, double **matrix_two, int matrix_column_one, int matrix_row_one, int matrix_column_two, int matrix_row_two);
	DLLDIR int** multiplicationInt(int **matrix_one, int **matrix_two, int matrix_column_one, int matrix_row_one, int matrix_column_two, int matrix_row_two);
}