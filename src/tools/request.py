from typing import Optional

from requests import get, post, Response


def request(
    url: str,
    method: Optional[str] = "get",
    params: Optional[dict] = {},
    headers: Optional[dict] = {},
    send_json: Optional[bool] = False,
    **kwargs
) -> Response:

    kwargs.update(url=url, headers=headers)
    method = method.lower()

    if method == "get":
        return get(data=params, **kwargs)
    elif method == "post":
        if send_json:
            return post(json=params, **kwargs)
        return post(data=params, **kwargs)
