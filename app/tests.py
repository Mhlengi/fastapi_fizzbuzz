from fastapi.testclient import TestClient

from .main import app
from .utils import get_fizz_buzz, get_placeholder_post

client = TestClient(app)


class TestUtilsFunctionGetFizzBuzz:
    def test_get_fizz_buzz_function_algorithm_returns_fizz_as_str(self):
        assert "Fizz" == get_fizz_buzz(3)

    def test_get_fizz_buzz_function_algorithm_returns_buzz_as_str(self):
        assert "Buzz" == get_fizz_buzz(5)

    def test_get_fizz_buzz_function_algorithm_returns_none_as_str(self):
        assert get_fizz_buzz(1) is None

    def test_get_fizz_buzz_function_algorithm_returns_fizz_buzz_as_str(self):
        assert "FizzBuzz" == get_fizz_buzz(15)


class TestUtilsFunctionGetPlaceholderPost:
    def test_get_placeholder_post_function_returns_what_as_string(self):
        expected_placeholder_post = get_placeholder_post(3)

        assert "title" in expected_placeholder_post
        assert "body" in expected_placeholder_post


class TestFizzBuzzApi:
    def test_get_fizzbuzz_list_api_with_limit_1(self):
        response = client.get("/fizzbuzz/?limit=1")

        expected_response_json = response.json()

        assert response.status_code == 200
        assert "number" in expected_response_json[0]
        assert "fizzbuzz" in expected_response_json[0]
        assert isinstance(expected_response_json, list)
        assert "placeholder_post" in expected_response_json[0]
        assert "body" in expected_response_json[0]["placeholder_post"]
        assert "title" in expected_response_json[0]["placeholder_post"]

    def test_get_fizzbuzz_retrieve_api_with_id_1(self):
        response = client.get("/fizzbuzz/1")

        expected_fizzbuzz_id = 1
        expected_fizzbuzz_value = None
        expected_response_json = response.json()

        assert response.status_code == 200
        assert isinstance(expected_response_json, dict)
        assert "number" in expected_response_json
        assert "fizzbuzz" in expected_response_json
        assert "placeholder_post" in expected_response_json
        assert "body" in expected_response_json["placeholder_post"]
        assert "title" in expected_response_json["placeholder_post"]
        assert expected_response_json["number"] == expected_fizzbuzz_id
        assert expected_response_json["fizzbuzz"] == expected_fizzbuzz_value

    def test_get_fizzbuzz_retrieve_api_with_multiple_of_3(self):
        expected_fizzbuzz_id = 3
        expected_fizzbuzz_value = "Fizz"

        response = client.get("/fizzbuzz/{}".format(expected_fizzbuzz_id))
        expected_response_json = response.json()

        assert response.status_code == 200
        assert isinstance(expected_response_json, dict)
        assert "number" in expected_response_json
        assert "fizzbuzz" in expected_response_json
        assert "placeholder_post" in expected_response_json
        assert "body" in expected_response_json["placeholder_post"]
        assert "title" in expected_response_json["placeholder_post"]
        assert expected_response_json["number"] == expected_fizzbuzz_id
        assert expected_response_json["fizzbuzz"] == expected_fizzbuzz_value

    def test_get_fizzbuzz_retrieve_api_with_multiple_of_5(self):
        response = client.get("/fizzbuzz/5")

        expected_fizzbuzz_id = 5
        expected_fizzbuzz_value = "Buzz"
        expected_response_json = response.json()

        assert response.status_code == 200
        assert isinstance(expected_response_json, dict)
        assert "number" in expected_response_json
        assert "fizzbuzz" in expected_response_json
        assert "placeholder_post" in expected_response_json
        assert "body" in expected_response_json["placeholder_post"]
        assert "title" in expected_response_json["placeholder_post"]
        assert expected_response_json["number"] == expected_fizzbuzz_id
        assert expected_response_json["fizzbuzz"] == expected_fizzbuzz_value

    def test_get_fizzbuzz_retrieve_api_with_multiple_of_both_3_and_5(self):
        response = client.get("/fizzbuzz/15")

        expected_fizzbuzz_id = 15
        expected_fizzbuzz_value = "FizzBuzz"
        expected_response_json = response.json()

        assert response.status_code == 200
        assert isinstance(expected_response_json, dict)
        assert "number" in expected_response_json
        assert "fizzbuzz" in expected_response_json
        assert "placeholder_post" in expected_response_json
        assert "body" in expected_response_json["placeholder_post"]
        assert "title" in expected_response_json["placeholder_post"]
        assert expected_response_json["number"] == expected_fizzbuzz_id
        assert expected_response_json["fizzbuzz"] == expected_fizzbuzz_value

    def test_get_fizzbuzz_retrieve_api_with_negative_id(self):
        response = client.get("/fizzbuzz/-1")

        expected_message = "ID must be a positive integer"

        assert response.status_code == 404
        assert response.json() == {"detail": expected_message}

    def test_get_fizzbuzz_retrieve_api_with_negative_limit_integer(self):
        response = client.get("/fizzbuzz/?limit=-1")

        expected_message = "Limit must be a positive integer"

        assert response.status_code == 404
        assert response.json() == {"detail": expected_message}
