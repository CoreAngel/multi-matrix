from tkinter import *
from tkinter import Tk, ttk
from enumTypes.ResultMatrixTypes import ResultMatrixTypes
from layouts.MatrixFrame import MatrixFrame
from layouts.ResultFrame import ResultFrame
from layouts.InfoFrame import InfoFrame
from interface.Result import ResultInterface


class Window:
    def __init__(self):
        self._main_frame = None
        self._matrix_frame = None
        self._result_frame = None
        self._info_frame = None
        self._results_interface = ResultInterface()

        self._root = Tk()
        self._root.geometry("400x550")
        self._root.title("Kalkulator mnozenia macierzy")
        self._root.iconbitmap('resources/icon.ico')
        self._root.resizable(width=False, height=False)
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_rowconfigure(0, weight=1)

        self._create_main_frame()

        self._matrix_frame = MatrixFrame(self._main_frame, self)
        self._matrix_frame.create_frame()

        self._result_frame = ResultFrame(self._main_frame, self)

        self._info_frame = InfoFrame(self._main_frame, self)

        self._root.protocol("WM_DELETE_WINDOW", self._on_close)

    def run(self):
        self._root.mainloop()

    def _create_main_frame(self):
        self._main_frame = ttk.Frame(self._root)
        self._main_frame['padding'] = (10, 10)
        self._main_frame.grid(column=0, row=0, sticky=N+E+S+W)
        self._main_frame.grid_columnconfigure(0, weight=1)
        self._main_frame.grid_rowconfigure(0, weight=1)
        self._main_frame.grid_rowconfigure(1, weight=1)
        self._main_frame.grid_rowconfigure(2, weight=1)

    def _on_close(self):
        self._result_frame.close_result_window(ResultMatrixTypes.ALL)
        self._root.destroy()

    def get_main_frame(self):
        return self._main_frame

    def get_matrix_frame(self):
        return self._matrix_frame

    def get_result_frame(self):
        return self._result_frame

    def get_info_frame(self):
        return self._info_frame

    def get_results_interface(self):
        return self._results_interface
