import json
from tkinter import PhotoImage, Tk

from classes import (
    CalculatableItem,
    Field,
    MainFrame,
    Manager,
    Resulter,
    ResultsFrame
)
# Creation of calculatable items
with open("items.json") as file_with_items:
    items = json.load(file_with_items)

cs_calculatable_items = []
for cross_section in items["cross_sections"]:
    cs_calculatable_items.append(CalculatableItem(
        cross_section["name"],
        cross_section["image_path"],
        cross_section["formula"],
        cross_section["parameters"],
        cross_section["constraints"],
    ))

ls_calculatable_items = []
for load_scheme in items["load_schemes"]:
    ls_calculatable_items.append(CalculatableItem(
        load_scheme["name"],
        load_scheme["image_path"],
        load_scheme["formula"],
        load_scheme["parameters"],
        load_scheme["constraints"],
    ))
# Creation of graphic interface
number_of_parameters_in_one_row = 4
number_of_rows = \
    len(cs_calculatable_items) // (number_of_parameters_in_one_row + 1) + \
    len(ls_calculatable_items) // (number_of_parameters_in_one_row + 1) + 2
# Main Window
root = Tk()
root.geometry(f"640x{505 + 31*number_of_rows+126}") # "adaptive" height
root.resizable(False, False)
root.title("MakhlaevSoftware - Beam deflection calculator")
# Main Window logo
image = PhotoImage(file="images/happy_deflection.png")
root.iconphoto(False, image)
# Cross section frame creation
cross_section_main_f = MainFrame(
    root,
    "Cross section",
    "Type of cross section",
    "Parameters of cross section"
)
cross_section_manager = Manager(
    cross_section_main_f,
    cs_calculatable_items
)
# Load scheme frame creation
load_scheme_main_f = MainFrame(
    root,
    "Load scheme",
    "Type of load scheme",
    "Parameters of load scheme"
)
load_scheme_manager = Manager(
    load_scheme_main_f,
    ls_calculatable_items
)
load_scheme_main_f.set_canvas_width(208)
# Results frame creation
results_f = ResultsFrame(root)
resulter = Resulter(
    results_f,
    cross_section_manager,
    load_scheme_manager
)

root.mainloop()
