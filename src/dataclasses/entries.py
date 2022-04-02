from dataclasses import dataclass
from tkinter import Entry, Text


@dataclass
class Entries:
    method: Entry
    url: Entry
    headers: Text
    json: Text
