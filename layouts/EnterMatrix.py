from tkinter import *
from tkinter import ttk
from enumTypes.EnterMatrixStates import EnterStates
from enumTypes.ResultMatrixTypes import ResultMatrixTypes
from enumTypes.ResultTimeTypes import ResultTimeTypes
from enumTypes.InfoTypes import InfoTypes
from enumTypes.CalculationStates import CalculationStates
from interface.Enter import EnterInterface
from exceptions.ErrorValue import ErrorValue
from threading import Thread


class EnterMatrix(ttk.Frame):
    def __init__(self, root, parent):
        super().__init__(root)
        self._parent = parent
        self._enter_interface = EnterInterface()

        self._var_label_text = StringVar()
        self._var_iterations = StringVar()
        self._text_field = None
        self._state = None

        self._var_button_text = StringVar()
        self._var_button = None


        self['relief'] = 'ridge'
        self['padding'] = (5, 5, 5, 5)
        self.grid(column=0, row=1, columnspan=2, sticky=W+E)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        Label(self, textvariable=self._var_label_text, height=2).grid(row=0, column=0, columnspan=2)
        self._text_field = Text(self, height=10, wrap=NONE)
        self._text_field.grid(row=1, column=0, columnspan=2, sticky=W+E)

        self._var_iterations.set(1)
        Label(self, text="Number of repetitions", height=2).grid(column=0, row=2)
        Entry(self, textvariable=self._var_iterations).grid(column=1, row=2)

        self._var_button = Button(self, textvariable=self._var_button_text, command=self._next_state)
        self._var_button.grid(row=3, column=0, pady=10)
        Button(self, text="Reset", command=self._reset).grid(row=3, column=1, pady=10)

        self._change_state(EnterStates.FIRST)
        self._update_texts()

    def _next_state(self):
        try:
            if self._state == EnterStates.FIRST:
                self._parent.get_result_frame().reset_matrices()
                matrix_one = self._enter_interface.create_matrix(self._text_field.get(1.0, END), EnterStates.FIRST)
                self._parent.get_results_interface().set_matrix(matrix_one, ResultMatrixTypes.FIRST)
                self._change_state(EnterStates.SECOND)
            elif self._state == EnterStates.SECOND:
                matrix_two = self._enter_interface.create_matrix(self._text_field.get(1.0, END), EnterStates.SECOND)
                self._parent.get_results_interface().set_matrix(matrix_two, ResultMatrixTypes.SECOND)

                self._calculate()

                self._change_state(EnterStates.FIRST)
        except ErrorValue as e:
            self._parent.get_info_frame().set_info(e.get_msg(), InfoTypes.ERROR)
        except Exception as e:
            self._parent.get_info_frame().set_info(str(e), InfoTypes.ERROR)
        else:
            self._parent.get_info_frame().hide_frame()

    def _reset(self):
        self._change_state(EnterStates.FIRST)
        self._text_field.delete(1.0, END)
        self._parent.get_info_frame().hide_frame()

    def _change_state(self, state):
        self._state = state
        self._update_texts()
        self._text_field.delete(1.0, END)

    def _update_texts(self):
        if self._state == EnterStates.FIRST:
            self._var_label_text.set("Provide the first matrix")
            self._var_button_text.set("Submit the matrix")
        elif self._state == EnterStates.SECOND:
            self._var_label_text.set("Provide the second matrix")
            self._var_button_text.set("Run the calculation")

    def _thread_calculate(self):
        result_interface = self._parent.get_results_interface()
        if result_interface.get_calculation_status() is True:
            return
        thread = Thread(target=self._calculate, daemon=True)
        thread.start()

    def _calculate(self):
        self._enter_interface.check_iteration(self._var_iterations.get())

        self._parent.get_results_interface().set_calculation_status(True)
        self._parent.get_matrix_frame().change_start_buttons_texts(CalculationStates.RUN)

        self._enter_interface.calculate()

        self._parent.get_result_frame().set_time(self._enter_interface.get_time_py(), ResultTimeTypes.PYTHON)
        self._parent.get_result_frame().set_time(self._enter_interface.get_time_cpp(), ResultTimeTypes.CPP)
        self._parent.get_result_frame().set_time(self._enter_interface.get_time_conv(), ResultTimeTypes.CONVERSION)

        self._parent.get_results_interface().set_matrix(self._enter_interface.get_result_matrix_py(), ResultMatrixTypes.RESULT_PY)
        self._parent.get_results_interface().set_matrix(self._enter_interface.get_result_matrix_cpp(), ResultMatrixTypes.RESULT_CPP)

        self._parent.get_results_interface().set_calculation_status(False)
        self._parent.get_matrix_frame().change_start_buttons_texts(CalculationStates.FINISH)

    def change_start_buttons(self, state):
        if state == CalculationStates.RUN:
            self._var_button_text.set("Calculating...")
            self._var_button.config(state="disabled")
        elif state == CalculationStates.FINISH:
            self._var_button_text.set("Submit the matrix")
            self._var_button.config(state="normal")

