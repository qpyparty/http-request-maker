from json import loads
from tkinter import END

from src.tools.request import request
from src.dataclasses import labels as lbl, entries as entr
from src.tools.reduction import reduce


def submit(labels: lbl.Labels, entries: entr.Entries) -> None:
    response = request(
        url=entries.url.get(),
        method=entries.method.get(),
        params=loads(entries.params.get("1.0", END)),
        headers=loads(entries.headers.get("1.0", END)),
        send_json=entries.send_json.get().lower() == "true",
    )

    labels.result.configure(text=reduce(response.text))
    labels.status.configure(text=str(response.status_code))
