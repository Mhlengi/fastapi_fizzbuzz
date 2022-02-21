import requests

BASE_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts/"


def get_fizz_buzz(number: int) -> str or object:
    """
    function that computes fizzbuzz algorithm

    :param number: int
    :return: str or obj
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return None


def get_placeholder_post(number: int) -> dict:
    """
    function that requests placeholder-post title and body

    :param number: int
    :return: {}
    """
    response = requests.get("{}{}".format(BASE_PLACEHOLDER_URL, number))
    if response.status_code == 200:
        json_response = response.json()
        title = json_response["title"] if "title" in json_response else ""
        body = json_response["body"] if "body" in json_response else ""
    else:
        title, body = "", ""
    return {"title": title, "body": body}
