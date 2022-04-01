from json import loads
from tkinter import END

from src.config.static import s7
from src.dataclasses import labels as lbl, entries as entr
from src.tools.reduction import reduce


def submit(labels: lbl.Labels, entries: entr.Entries) -> None:
    response = s7.request(
        entries.method.get(),
        entries.url.get(),
        headers=loads(entries.headers.get("1.0", END)),
        json=loads(entries.json.get("1.0", END)),
    )

    labels.result.configure(text=reduce(response.text))
    labels.status.configure(text=str(response.status_code))
