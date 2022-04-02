from tkinter import Tk, Entry, Text

from src.dataclasses.entries import Entries
from src.tools import create_element as create


def setup(root: Tk) -> Entries:
    url = create.widget(Entry, width=50, insertbackground="white")
    url.insert(0, "https://google.com/")

    method = create.widget(Entry, width=10, insertbackground="white")
    method.insert(0, "get")

    send_json = create.widget(Entry, width=10, insertbackground="white")
    send_json.insert(0, "false")

    headers = create.widget(Text, height=15, width=100, insertbackground="white")
    headers.insert(1.0, "{}")

    params = create.widget(Text, height=20, width=100, insertbackground="white")
    params.insert(1.0, "{}")

    method.grid(column=0, row=4)
    url.grid(column=0, row=5)
    send_json.grid(column=0, row=6)
    headers.grid(column=0, row=7)
    params.grid(column=0, row=8)

    del root
    return Entries(**locals())
