from tkinter import END, Listbox


class MyListbox(Listbox):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

    def fill(self, names):
        for name in names:
            self.insert(END, name)

    def reset(self):
        self.select_clear(0, "end")
        self.see(0)

    def set_callback_on_selection(self, function):
        self.bind("<<ListboxSelect>>", function)
