from tkinter import *
from tkinter import ttk
from enumTypes.InfoTypes import InfoTypes


class InfoFrame(ttk.Frame):
    def __init__(self, root, parent):
        super().__init__(root, height=31)
        self._parent = parent

        self._info_label = None
        self._image_label = None

        self['relief'] = 'ridge'
        self['padding'] = (5, 5)
        self.grid(row=2, column=0, sticky=W+E+S)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._image_label = Label(self, text="")
        self._image_label.grid(row=0, column=0)
        self._info_label = Label(self, text="")
        self._info_label.grid(row=0, column=1, sticky=W+S)

        self.hide_frame()

    class SetInfoAppearance:
        def __init__(self, decorator):
            self._decorator = decorator

        def __call__(self, info_text, info_type, photo_label, text_label):
            photo_error = PhotoImage(file="resources/error.png")
            photo_info = PhotoImage(file="resources/info.png")

            if info_type == InfoTypes.ERROR:
                photo_label.config(image=photo_error)
                photo_label.photo = photo_error
                text_label.config(fg="red")
            else:
                photo_label.config(image=photo_info)
                photo_label.photo = photo_info
                text_label.config(fg="blue")

            self._decorator(info_text, info_type, photo_label, text_label)

    def set_info(self, info_text, info_type):
        self._set_info_text(info_text, info_type, self._image_label, self._info_label)
        self.show_frame()

    def hide_frame(self):
        self._info_label.grid_remove()
        self._image_label.grid_remove()

    def show_frame(self):
        self._info_label.grid()
        self._image_label.grid()

    @SetInfoAppearance
    def _set_info_text(info_text, info_type, photo_label, text_label):
        text_label.configure(text=info_text)

