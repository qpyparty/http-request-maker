from tkinter import Button, Tk

from src.elements import labels, entries
from src.functions.submit import submit as submit_cmd
from src.tools import create_element as create


def setup(root: Tk) -> None:

    lbls = labels.setup(root)
    entrs = entries.setup(root)

    submit = create.widget(
        Button,
        text="Отправить",
        activebackground="grey",
        command=lambda: submit_cmd(lbls, entrs)
    )

    submit.grid(column=0, row=3)
