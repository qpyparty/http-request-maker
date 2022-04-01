from tkinter import Tk, Entry, Text

from src.dataclasses.entries import Entries


def setup(root: Tk) -> Entries:
    method = Entry(root, width=10)
    method.insert(0, "get")

    url = Entry(root, width=50)
    url.insert(0, "https://google.com/")

    headers = Text(root, height=15, width=100)
    headers.insert(1.0, "{}")

    json = Text(root, height=20, width=100)
    json.insert(1.0, "{}")

    method.grid(column=0, row=4)
    url.grid(column=0, row=5)
    headers.grid(column=0, row=6)
    json.grid(column=0, row=7)

    del root
    return Entries(**locals())
