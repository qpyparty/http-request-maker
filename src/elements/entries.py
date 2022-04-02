from tkinter import Tk, Entry, Text

from src.dataclasses.entries import Entries


def setup(root: Tk) -> Entries:
    url = Entry(root, width=50)
    url.insert(0, "https://google.com/")

    method = Entry(root, width=10)
    method.insert(0, "get")
    
    send_json = Entry(root, width=10)
    send_json.insert(0, "0")

    headers = Text(root, height=15, width=100)
    headers.insert(1.0, "{}")

    params = Text(root, height=20, width=100)
    params.insert(1.0, "{}")

    method.grid(column=0, row=4)
    url.grid(column=0, row=5)
    send_json.grid(column=0, row=6)
    headers.grid(column=0, row=7)
    params.grid(column=0, row=8)

    del root
    return Entries(**locals())
