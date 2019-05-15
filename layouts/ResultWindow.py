from tkinter import *
from tkinter import Tk, ttk


class ResultWindow:
    def __init__(self, title, matrix):
        self._root = None
        self._main_frame = None
        self._canvas = None
        self._canvas_frame = None

        self._columns = None
        self._rows = None

        try:
            self._root = Tk()
            self._root.geometry("300x300")
            self._root.title(title)
            self._root.iconbitmap('resources/icon.ico')
            self._root.columnconfigure(0, weight=1)
            self._root.rowconfigure(0, weight=1)

            self._main_frame = Frame(self._root)
            self._main_frame.grid(row=0, column=0, sticky=N+S+W+E)
            self._main_frame.rowconfigure(0, weight=1)
            self._main_frame.columnconfigure(0, weight=1)

            self._canvas = Canvas(self._main_frame, bg='white')
            self._canvas.grid(row=0, column=0, sticky=N+S+W+E)

            self._canvas_frame = Frame(self._main_frame)
            self._canvas_frame.grid(row=0, column=0, sticky=W+E+S+W)
            self._canvas.create_window(0, 0, window=self._canvas_frame, anchor=N + W)

            vbar = Scrollbar(self._main_frame, orient=VERTICAL)
            vbar.grid(row=0, column=1, rowspan=2, sticky=N+W+S)
            vbar.config(command=self._canvas.yview)
            self._canvas.config(yscrollcommand=vbar.set)

            hbar = Scrollbar(self._main_frame, orient=HORIZONTAL)
            hbar.grid(row=1, column=0, sticky=E+W+S)
            hbar.config(command=self._canvas.xview)
            self._canvas.config(xscrollcommand=hbar.set)

            self._get_size(matrix)
            self._create_axis()
            self._create_grid_table(matrix)

            self._main_frame.bind("<Configure>", self._set_scroll_operation)
            self._main_frame.bind_all("<MouseWheel>", self._on_vertical_scroll)
            self._main_frame.bind_all("<Control-MouseWheel>", self._on_horizontal_scroll)
        except Exception:
            print("Create result window failed!!!")

    def run(self):
        self._root.mainloop()

    def _set_scroll_operation(self, event):
        self._canvas.configure(scrollregion=self._canvas_frame.bbox("all"))

    def _on_vertical_scroll(self, event):
        if self._canvas.yview() == (0.0, 1.0):
            return

        position = int(-1 * (event.delta / 120))
        self._canvas.yview_scroll(position, "units")

    def _on_horizontal_scroll(self, event):
        if self._canvas.xview() == (0.0, 1.0):
            return

        position = int(-1 * (event.delta / 120))
        self._canvas.xview_scroll(position, "units")

    def _create_grid_table(self, matrix):
        for i in range(self._rows):
            for j in range(self._columns):
                Label(self._canvas_frame, text=matrix[i][j], font=('times', 13, 'bold'), borderwidth=2, relief="groove").grid(column=j+1, row=i+1, sticky=W+S+E+N)

    def _create_axis(self):
        for i in range(self._rows):
            frame = ttk.Frame(self._canvas_frame)
            frame['relief'] = 'groove'
            frame['padding'] = (2, 2)
            frame.grid(row=i+1, column=0, sticky=W+S+E+N)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)

            Label(frame, text=i, font=('times', 13, 'bold'), bg="grey").grid(column=0, row=0, sticky=W+S+E+N)

        for i in range(self._columns):
            frame = ttk.Frame(self._canvas_frame)
            frame['relief'] = 'groove'
            frame['padding'] = (2, 2)
            frame.grid(row=0, column=i+1, sticky=W+S+E+N)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)

            Label(frame, text=i, font=('times', 13, 'bold'), bg="grey").grid(column=0, row=0, sticky=W+S+E+N)

    def _get_size(self, matrix):
        self._rows = len(matrix)
        if self._rows <= 0:
            raise ValueError("Incorrect size of the matrix!")

        self._columns = len(matrix[0])
        if self._columns <= 0:
            raise ValueError("Incorrect size of the matrix!")

    def get_root(self):
        return self._root

