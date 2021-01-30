from math import pi
from tkinter import messagebox

from .modalwindowgraph import ModalWindowGraph


class Resulter:
    def __init__(self, r_f, J_m, v_m):
        J_m.set_callback_on_text_change(self.clear_J)
        self._J_m = J_m
        v_m.set_callback_on_text_change(self.clear_v)
        self._v_m = v_m

        self._J = None
        self._J_f = r_f.get_J_field()
        self._v = None
        self._v_f = r_f.get_v_field()

        g_b = r_f.get_graph_button()
        g_b.config(command=self.graph)
        self._g_b = g_b

        r_b = r_f.get_reset_button()
        r_b.config(command=self.reset)
        self._r_b = r_b

        c_b = r_f.get_calculate_button()
        c_b.config(command=self.calculate)
        self._c_b = c_b

    def clear_J(self, sv):
        self._J_f.activate()
        self._J_f.clear_text()
        self._J_f.disable()
        self._g_b["state"] = "disabled"
        self.clear_v(None)

    def clear_v(self, sv):
        self._v_f.activate()
        self._v_f.clear_text()
        self._v_f.disable()
        self._g_b["state"] = "disabled"

    def graph(self):
        c_a = self._v_m.get_current_active()
        params = c_a.get_simplified_parameters()
        # Finding z range for graph
        tmp = c_a.constraints[0].split("<=")
        z_max = int(eval(tmp[2].strip(), params) * 10**3 + 1)
        z_values = range(0, z_max)
        # Finding v values for z correspondingly
        v_values = [self._v_m.calculate({"J": self._J, "z": z / 10**3}) * 10**3 \
            for z in z_values]
        # Create modal window with a graph
        ModalWindowGraph(z_values, v_values, c_a.name)

    def reset(self):
        self._J_m.reset()
        self._v_m.reset()
        self.clear_J(None)
        self.clear_v(None)
        self._g_b["state"] = "disabled"

    def calculate(self):
        J = self._J_m.calculate({"pi": pi})

        if J is not None:
            self._J_f.activate()
            self._J_f.set_text(round(J * 10**12))
            self._J_f.readonly()

            self._J = J

            v = self._v_m.calculate({"J": J})
            if v is not None:
                self._v_f.activate()
                self._v_f.set_text(v * 10**3)
                self._v_f.readonly()

                self._g_b["state"] = "normal"

                self._v = v
            else:
                self._v_f.activate()
                self._v_f.clear_text()
                self._v_f.disable()

                self._g_b["state"] = "disabled"

                self._v = None
        else:
            self._J_f.activate()
            self._J_f.clear_text()
            self._J_f.disable()

            self._v_f.activate()
            self._v_f.clear_text()
            self._v_f.disable()

            self._g_b["state"] = "disabled"

            self._J = None
            self._v = None

        if self._J_m.is_active() and self._J is not None and \
            not self._v_m.is_active() or self._v is not None:
            pass
        else:
            messagebox.showwarning("Achtung", "Missing or wrong parameters")
