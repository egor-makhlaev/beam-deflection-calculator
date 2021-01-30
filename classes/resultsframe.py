from tkinter import (
    Button,
    Entry,
    Frame,
    LEFT,
    Label,
    LabelFrame,
    RIGHT,
    TOP,
    X
)

from .field import Field


class ResultsFrame:
    @staticmethod
    def create_field(fields_f, name, measurement):
        main_f = Frame(fields_f)
        main_f.pack(pady=5)

        left_lb = Label(main_f, text=f"{name} :")
        left_lb.pack(side=LEFT)

        e = Entry(main_f, state='disabled', width=29)
        e.pack(side=LEFT)

        right_lb = Label(main_f, text=measurement)
        right_lb.pack(side=LEFT)

        return Field(left_lb, None, e, right_lb)

    def __init__(self, root):
        results_f = LabelFrame(root, text="Results")
        results_f.pack(side=TOP, fill=X, padx=10, pady=5)

        tmp_f = Frame(results_f)
        tmp_f.pack(fill=X, pady=1)

        fields_f = Frame(tmp_f)
        fields_f.pack(side=LEFT, padx=46)

        self._J_field = ResultsFrame.create_field(fields_f, "J", "mm⁴")
        self._v_field = ResultsFrame.create_field(fields_f, "v", "mm  ")

        buttons_f = Frame(results_f)
        buttons_f.pack(fill=X, padx=10)

        calculate_b = Button(buttons_f, text="Calculate", width=10)
        calculate_b.pack(side=RIGHT, pady=5)
        self._c_b = calculate_b

        reset_b = Button(buttons_f, text="Reset", width=10)
        reset_b.pack(side=RIGHT, padx=3, pady=5)
        self._r_b = reset_b

        graph_b = Button(buttons_f, text="Graph", width=10)
        graph_b.pack(side=RIGHT, pady=5)
        graph_b["state"] = "disabled"
        self._g_b = graph_b

    def get_J_field(self):
        return self._J_field

    def get_v_field(self):
        return self._v_field

    def get_calculate_button(self):
        return self._c_b

    def get_reset_button(self):
        return self._r_b

    def get_graph_button(self):
        return self._g_b
