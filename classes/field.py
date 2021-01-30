class Field:
    def __init__(self, left_lb, sv, e, right_lb):
        self._parameter = None
        self._left_lb = left_lb
        self._sv = sv
        self._e = e
        self._right_lb = right_lb

    def set_parameter(self, parameter):
        self._parameter = parameter

    def get_parameter(self):
        return self._parameter

    def set_left_lb_text(self, text):
        self._left_lb.config(text=f"{text} :")

    def set_right_lb_text(self, text):
        self._right_lb.config(text=text)

    def set_text(self, text):
        self.clear_text()
        self._e.insert(0, text)

    def get_text(self):
        return self._e.get()

    def clear_text(self):
        self._e.delete(0, "end")

    def set_callback_on_text_change(self, callback):
        self._sv.trace("w", lambda name, index, mode, sv=self._sv: callback(sv))

    def activate(self):
        self._e["state"] = "normal"

    def disable(self):
        self._e["state"] = "disable"

    def readonly(self):
        self._e["state"] = "readonly"
