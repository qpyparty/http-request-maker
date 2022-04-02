from tkinter import Tk, Label

from src.dataclasses.labels import Labels
from src.tools import create_element as create


def setup(root: Tk) -> Labels:
    result = create.widget(Label, text="")
    status = create.widget(Label, text="")

    result.grid(column=0, row=1)
    status.grid(column=0, row=2)

    del root
    return Labels(**locals())
