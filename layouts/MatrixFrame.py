from tkinter import *
from tkinter import ttk, StringVar
from enumTypes.EnterMatrixTypes import EnterMatrixTypes
from layouts.RandomMatrix import RandomMatrix
from layouts.EnterMatrix import EnterMatrix


class MatrixFrame(ttk.Frame):
    def __init__(self, root, parent):
        super().__init__(root)
        self._parent = parent

        self._random_matrix = None
        self._enter_matrix = None

        self._radio_buttons = [
            ("Losowe wartości", "random", lambda: self._change_matrix_frame(EnterMatrixTypes.RANDOM)),
            ("Wprowadź macierz", "enter", lambda: self._change_matrix_frame(EnterMatrixTypes.ENTER))
        ]
        self._radio_field = StringVar()
        self._radio_field.set("random")

    def create_frame(self):
        self['padding'] = (0, 10)
        self.grid(row=0, column=0, sticky=W+E+N)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        for index, (text, mode, function) in enumerate(self._radio_buttons):
            Radiobutton(self, text=text, variable=self._radio_field, value=mode, command=function).grid(column=index, row=0)

        self._random_matrix = RandomMatrix(self, self._parent)
        self._enter_matrix = EnterMatrix(self, self._parent)
        self._enter_matrix.grid_remove()

    def _change_matrix_frame(self, matrix_type):
        if matrix_type == EnterMatrixTypes.RANDOM:
            self._enter_matrix.grid_remove()
            self._random_matrix.grid()
        else:
            self._random_matrix.grid_remove()
            self._enter_matrix.grid()

    def change_start_buttons_texts(self, state):
        self._random_matrix.change_start_buttons(state)
        self._enter_matrix.change_start_buttons(state)

