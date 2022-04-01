from json import loads
from tkinter import END

from fake_useragent import UserAgent

from src.config.static import s7
from src.dataclasses import labels as lbl, entries as entr
from src.tools.reduction import reduce


def submit(labels: lbl.Labels, entries: entr.Entries) -> None:
    params = dict(
        method=entries.method.get(),
        url=entries.url.get(),
        json=loads(entries.json.get("1.0", END)),
    )
    headers = loads(entries.headers.get("1.0", END))
    if headers:
        response = s7.request(headers=headers, **params)
    else:
        response = s7.request(headers={"User-Agent": UserAgent().random}, **params)

    labels.result.configure(text=reduce(response.text))
    labels.status.configure(text=str(response.status_code))
