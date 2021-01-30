from tkinter import (
    Toplevel,
    PhotoImage,
    TOP,
    BOTH
)
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class ModalWindowGraph(Toplevel):
    def __init__(self, x_values, y_values, name_of_item):
        super().__init__()
        
        self.grab_set()
        self.focus_set()
        self.geometry(f"640x640")
        self.resizable(False, False)
        self.title("MakhlaevSoftware - Graphic")
        image = PhotoImage(file="images/happy_deflection.png")
        self.iconphoto(False, image)

        fig = Figure(figsize=(5, 5), dpi=100)
        a = fig.add_subplot(111)
        a.set_title(name_of_item + "\nDeflection v with respect to position z")
        a.set_xlabel("Position z (mm)")
        a.set_ylabel("Deflection v (mm)")
        a.margins(0)
        a.plot(x_values, y_values)

        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
