from tkinter import *
from tkinter import ttk
from enumTypes.LootsTypes import LootsTypes
from enumTypes.InfoTypes import InfoTypes
from enumTypes.ResultMatrixTypes import ResultMatrixTypes
from enumTypes.ResultTimeTypes import ResultTimeTypes
from enumTypes.CalculationStates import CalculationStates
from interface.Random import RandomInterface
from exceptions.ErrorValue import ErrorValue
from threading import Thread


class RandomMatrix(ttk.Frame):
    def __init__(self, root, parent):
        super().__init__(root)
        self._parent = parent

        self._first_matrix = None
        self._second_matrix = None
        self._iterations = None
        self._type_of_numbers = None
        self._interval_from = None
        self._interval_to = None

        self._var_button_text = StringVar()
        self._var_button_text.set("Uruchom obliczenia")
        self._var_button = None

        self['relief'] = 'ridge'
        self['padding'] = (5, 5, 5, 5)
        self['borderwidth'] = 2
        self.grid(column=0, row=1, columnspan=2, sticky=W+E)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._first_matrix = StringVar()
        Label(self, text="Wymiary macierzy 1 (W K)", height=2).grid(column=0, row=0)
        Entry(self, textvariable=self._first_matrix).grid(column=1, row=0)

        self._second_matrix = StringVar()
        Label(self, text="Wymiary macierzy 2 (W K)", height=2).grid(column=0, row=1)
        Entry(self, textvariable=self._second_matrix).grid(column=1, row=1)

        self._iterations = StringVar()
        self._iterations.set(1)
        Label(self, text="Liczba powtórzeń", height=2).grid(column=0, row=2)
        Entry(self, textvariable=self._iterations).grid(column=1, row=2)

        self._radio_buttons = [
            ("Liczby rzeczywiste", LootsTypes.REAL),
            ("Liczby całkowite", LootsTypes.INTEGER)
        ]
        self._type_of_numbers = StringVar()
        self._type_of_numbers.set(LootsTypes.REAL)

        for index, (text, mode) in enumerate(self._radio_buttons):
            Radiobutton(self, text=text, variable=self._type_of_numbers, value=mode).grid(column=index, row=3)

        Label(self, text="Przedział od - do", height=2).grid(column=0, row=4, columnspan=2, sticky=W+E)

        self._interval_from = StringVar()
        self._interval_from.set(0)
        self._interval_to = StringVar()
        self._interval_to.set(100)
        Entry(self, textvariable=self._interval_from).grid(column=0, row=5)
        Entry(self, textvariable=self._interval_to).grid(column=1, row=5)

        self._var_button = Button(self, textvariable=self._var_button_text, command=self._on_click)
        self._var_button.grid(row=6, pady=10, columnspan=2)

    def _on_click(self):
        result_interface = self._parent.get_results_interface()
        if result_interface.get_calculation_status() is True:
            return
        thread = Thread(target=self._calculate, daemon=True)
        thread.start()

    def _calculate(self):
        random_interface = RandomInterface()
        try:
            random_interface.check_size(self._first_matrix.get(), self._second_matrix.get())
            random_interface.check_iteration(self._iterations.get(), self._type_of_numbers.get())
            random_interface.check_interval(self._interval_from.get(), self._interval_to.get())
        except ErrorValue as e:
            self._parent.get_info_frame().set_info(e.get_msg(), InfoTypes.ERROR)
        except Exception as e:
            self._parent.get_info_frame().set_info(str(e), InfoTypes.ERROR)
        else:
            self._parent.get_info_frame().hide_frame()
            self._parent.get_results_interface().set_calculation_status(True)
            self._parent.get_matrix_frame().change_start_buttons_texts(CalculationStates.RUN)
            matrix_one = random_interface.create_matrix_one()
            matrix_two = random_interface.create_matrix_two()
            self._parent.get_results_interface().set_matrix(matrix_one, ResultMatrixTypes.FIRST)
            self._parent.get_results_interface().set_matrix(matrix_two, ResultMatrixTypes.SECOND)

            random_interface.calculate()

            self._parent.get_result_frame().set_time(random_interface.get_time_py(), ResultTimeTypes.PYTHON)
            self._parent.get_result_frame().set_time(random_interface.get_time_cpp(), ResultTimeTypes.CPP)
            self._parent.get_result_frame().set_time(random_interface.get_time_conv(), ResultTimeTypes.CONVERSION)

            self._parent.get_results_interface().set_matrix(random_interface.get_result_matrix_py(), ResultMatrixTypes.RESULT_PY)
            self._parent.get_results_interface().set_matrix(random_interface.get_result_matrix_cpp(), ResultMatrixTypes.RESULT_CPP)

            self._parent.get_results_interface().set_calculation_status(False)
            self._parent.get_matrix_frame().change_start_buttons_texts(CalculationStates.FINISH)

    def change_start_buttons(self, state):
        if state == CalculationStates.RUN:
            self._var_button_text.set("Obliczam...")
            self._var_button.config(state="disabled")
        elif state == CalculationStates.FINISH:
            self._var_button_text.set("Uruchom obliczenia")
            self._var_button.config(state="normal")

