from tkinter import Widget
from typing import Type


def widget(wdgt: Type[Widget], **kwargs):
    from src.app import root

    return wdgt(root, fg="white", bg="black", **kwargs)
