from tkinter import Button, Tk

from src.elements import labels, entries
from src.functions.submit import submit as submit_cmd


def setup(root: Tk) -> None:

    lbls = labels.setup(root)
    entrs = entries.setup(root)

    submit = Button(root, text="Отправить", command=lambda: submit_cmd(lbls, entrs))

    submit.grid(column=0, row=3)
