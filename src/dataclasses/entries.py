from dataclasses import dataclass
from tkinter import Entry, Text


@dataclass
class Entries:
    url: Entry
    method: Entry
    send_json: Entry
    headers: Text
    params: Text
