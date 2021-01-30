from tkinter import (
    Entry,
    Frame,
    LEFT,
    Label,
    LabelFrame,
    RIGHT,
    SINGLE,
    Scrollbar,
    StringVar,
    TOP,
    VERTICAL,
    W,
    X
)

from .mylistbox import MyListbox
from .mycanvas import MyCanvas
from .field import Field


class MainFrame:
    def __init__(self, root, main_f_text, type_f_text, enter_f_text):
        x = 10
        y = 5
        # Main Frame
        main_f = LabelFrame(root, text=main_f_text)
        main_f.pack(side=TOP, fill=X, padx=x, pady=5, ipady=5)
        # Type of ... Frame
        type_f = LabelFrame(main_f, text=type_f_text)
        type_f.pack(side=TOP, fill=X, padx=x, pady=1)
        # Frame for Listbox and Scrollbar
        listbox_scroll_f = Frame(type_f)
        listbox_scroll_f.pack(side=LEFT, padx=5, pady=y)
        # Listbox
        lb = MyListbox(
            listbox_scroll_f,
            width=57,
            height=9,
            selectmode=SINGLE,
            activestyle="none",
            borderwidth=0,
            highlightthickness=0,
        )
        lb.pack(side=LEFT)
        self._listbox = lb
        # Scrollbar
        yscroll = Scrollbar(listbox_scroll_f, command=lb.yview, orient=VERTICAL)
        yscroll.pack(side=LEFT, fill="y")
        lb.configure(yscrollcommand=yscroll.set)
        # Canvas for PhotoImage
        c = MyCanvas(type_f, width=146, height=146, bg="white")
        c.pack(side=RIGHT, padx=5, pady=y)
        self._canvas = c
        # Parameters of ... Frame
        enter_f = LabelFrame(main_f, text=enter_f_text)
        enter_f.pack(side=TOP, fill=X, padx=x, pady=5)
        self._enter_f = enter_f

    def get_listbox(self):
        return self._listbox

    def get_canvas(self):
        return self._canvas

    def set_canvas_width(self, width):
        self._canvas.config(width=width)

    def get_parameters_fields(self, number_of_parameters):
        number_of_parameters_in_one_row = 4
        fields = []

        for i in range(0, number_of_parameters):
            row = i // number_of_parameters_in_one_row
            column = i % number_of_parameters_in_one_row

            field_f = Frame(self._enter_f)
            field_f.grid(row=row, column=column, sticky=W, padx=35, pady=5)

            left_lb = Label(field_f)
            left_lb.pack(side=LEFT)

            sv = StringVar()
            e = Entry(field_f, state='disabled', width=4, textvariable=sv)
            e.pack(side=LEFT)

            right_lb = Label(field_f)
            right_lb.pack(side=LEFT)

            fields.append(Field(left_lb, sv, e, right_lb))

        return fields
