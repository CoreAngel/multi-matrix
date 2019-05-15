from tkinter import *
from tkinter import ttk
from layouts.ResultWindow import ResultWindow
from enumTypes.ResultMatrixTypes import ResultMatrixTypes
from enumTypes.InfoTypes import InfoTypes
from enumTypes.ResultTimeTypes import ResultTimeTypes


class ResultFrame(ttk.Frame):
    def __init__(self, root, parent):
        super().__init__(root)
        self._parent = parent

        self._var_time_python = None
        self._var_time_cpp = None
        self._var_time_conversion = None

        self._window_matrix_one = None
        self._window_matrix_two = None
        self._window_result_py = None
        self._window_result_cpp = None

        self['relief'] = 'ridge'
        self['padding'] = (5, 10)
        self.grid(row=1, column=0, sticky=W+E+N)
        self.grid_columnconfigure(0, weight=1)

        self._create_measurement_frame()
        self._create_result_frame()

    def _create_measurement_frame(self):
        frame = Frame(self)
        frame.grid(row=1, sticky=W+E)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        Label(frame, text="Calculation times").grid(row=0, columnspan=3)

        self._var_time_python = StringVar()
        self._var_time_python.set("-")
        Label(frame, text="Python").grid(row=1, column=0)
        Label(frame, textvariable=self._var_time_python).grid(row=2, column=0)

        self._var_time_cpp = StringVar()
        self._var_time_cpp.set("-")
        Label(frame, text="C++").grid(row=1, column=1)
        Label(frame, textvariable=self._var_time_cpp).grid(row=2, column=1)

        self._var_time_conversion = StringVar()
        self._var_time_conversion.set("-")
        Label(frame, text="Conversion").grid(row=1, column=2)
        Label(frame, textvariable=self._var_time_conversion).grid(row=2, column=2)

    def _create_result_frame(self):
        frame = Frame(self)
        frame.grid(row=2, sticky=W+E, pady=10)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        Label(frame, text="Matrices").grid(row=0, columnspan=4)

        Button(frame, text="Matrix 1", width=10, command=lambda: self._open_result_window(ResultMatrixTypes.FIRST)).grid(row=1, column=0)

        Button(frame, text="Matrix 2", width=10, command=lambda: self._open_result_window(ResultMatrixTypes.SECOND)).grid(row=1, column=1)

        Button(frame, text="Result Py", width=10, command=lambda: self._open_result_window(ResultMatrixTypes.RESULT_PY)).grid(row=1, column=2)

        Button(frame, text="Result Cpp", width=10, command=lambda: self._open_result_window(ResultMatrixTypes.RESULT_CPP)).grid(row=1, column=3)

    def _open_result_window(self, matrix_type):
        matrix = self._parent.get_results_interface().get_matrix(matrix_type)
        if matrix is None:
            self._parent.get_info_frame().set_info("The matrix is ​​empty", InfoTypes.INFO)
            return

        if len(matrix) * len(matrix[0]) > 2500:
            self._parent.get_info_frame().set_info("The matrix is ​​too large to display it", InfoTypes.INFO)
            return

        self._parent.get_info_frame().hide_frame()

        if matrix_type == ResultMatrixTypes.FIRST:
            title = "First matrix"
            self.close_result_window(ResultMatrixTypes.FIRST)
            self._window_matrix_one = ResultWindow(title, matrix)
            self._window_matrix_one.run()
        elif matrix_type == ResultMatrixTypes.SECOND:
            title = "Second matrix"
            self.close_result_window(ResultMatrixTypes.SECOND)
            self._window_matrix_two = ResultWindow(title, matrix)
            self._window_matrix_two.run()
        elif matrix_type == ResultMatrixTypes.RESULT_PY:
            title = "Result matrix python"
            self.close_result_window(ResultMatrixTypes.RESULT_PY)
            self._window_result_py = ResultWindow(title, matrix)
            self._window_result_py.run()
        elif matrix_type == ResultMatrixTypes.RESULT_CPP:
            title = "Result matrix C++"
            self.close_result_window(ResultMatrixTypes.RESULT_CPP)
            self._window_result_cpp = ResultWindow(title, matrix)
            self._window_result_cpp.run()

    def set_time(self, time, time_type):
        self._parent.get_results_interface().set_time(time, time_type)

        unit = "s"
        if time <= 1:
            time *= 1000
            unit = "ms"

        time = '{0:.3f}'.format(time)
        if time_type == ResultTimeTypes.PYTHON:
            self._var_time_python.set(time + " " + unit)
        elif time_type == ResultTimeTypes.CPP:
            self._var_time_cpp.set(time + " " + unit)
        elif time_type == ResultTimeTypes.CONVERSION:
            self._var_time_conversion.set(time + " " + unit)

    def reset_matrices(self):
        self._parent.get_results_interface().reset_matrices()

    def reset_times(self):
        self._var_time_python.set("-")
        self._var_time_cpp.set("-")
        self._var_time_conversion.set("-")

    def close_result_window(self, result_matrix_type):
        try:
            if (result_matrix_type == ResultMatrixTypes.FIRST or result_matrix_type == ResultMatrixTypes.ALL) and self._window_matrix_one is not None:
                self._window_matrix_one.get_root().destroy()
            if (result_matrix_type == ResultMatrixTypes.SECOND or result_matrix_type == ResultMatrixTypes.ALL) and self._window_matrix_two is not None:
                self._window_matrix_two.get_root().destroy()
            if (result_matrix_type == ResultMatrixTypes.RESULT_PY or result_matrix_type == ResultMatrixTypes.ALL) and self._window_result_py is not None:
                self._window_result_py.get_root().destroy()
            if (result_matrix_type == ResultMatrixTypes.RESULT_CPP or result_matrix_type == ResultMatrixTypes.ALL) and self._window_result_cpp is not None:
                self._window_result_cpp.get_root().destroy()
        except Exception:
            pass






