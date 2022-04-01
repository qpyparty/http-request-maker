from tkinter import Tk, Label

from src.dataclasses.labels import Labels


def setup(root: Tk) -> Labels:
    result = Label(root, text="")
    status = Label(root, text="")

    result.grid(column=0, row=1)
    status.grid(column=0, row=2)

    del root
    return Labels(**locals())
