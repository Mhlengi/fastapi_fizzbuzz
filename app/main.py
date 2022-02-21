from typing import Optional

from fastapi import FastAPI, HTTPException

from .utils import get_fizz_buzz, get_placeholder_post

app = FastAPI()


@app.get("/fizzbuzz")
def list_fizzbuzz(limit: Optional[int] = 10) -> list[dict]:
    """
    api function view that returns a list of fizz-buzz objects

    :param limit: int
    :return: []
    """
    if limit <= 0:
        message = "Limit must be a positive integer"
        raise HTTPException(status_code=404, detail=message)

    _list = list()
    for number in range(1, limit + 1):
        content = {
            "number": number,
            "fizzbuzz": get_fizz_buzz(number),
            "placeholder_post": get_placeholder_post(number),
        }
        _list.append(content)
    return _list


@app.get("/fizzbuzz/{fizzbuzz_id}")
def retrieve_fizzbuzz(fizzbuzz_id: int) -> dict:
    """
    api function view that returns a detail of fizz-buzz object

    :param fizzbuzz_id: int
    :return: {}
    """
    if fizzbuzz_id <= 0:
        message = "ID must be a positive integer"
        raise HTTPException(status_code=404, detail=message)

    content = {
        "number": fizzbuzz_id,
        "fizzbuzz": get_fizz_buzz(fizzbuzz_id),
        "placeholder_post": get_placeholder_post(fizzbuzz_id),
    }
    return content
