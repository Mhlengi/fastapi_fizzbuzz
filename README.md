# FastAPI FizzBuzz

## Requirements
- Python 3.9+
- Docker(Optional)

Please consult Google if you need to install any of the pre-requisites

## Set Up Installation
- Clone/Download the git repo - `git clone https://github.com/Mhlengi/fastapi_fizzbuzz`
- Navigate to the project folder`fastapi_fizzbuzz`
- Install python3 `brew install python3`
- Install pip3 `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate a virtual environment: `. venv/bin/activate`
- Install all the python dependencies `pip install -r requirements.txt`
- Run the local server with `uvicorn app.main:app --reload`

## Interactive API docs or Alternative API docs(redoc)   
- Now go to [localhost home application(docs)](http://127.0.0.1:8000/docs)
- or Alternative [localhost home application(redoc)](http://127.0.0.1:8000/redoc)
- To list all FizzBuzz objects from Api request, use `GET` http Method.
- `GET(List)` endpoint `http://127.0.0.1:8000/fizzbuzz`
- ![GET LIST API](https://github.com/Mhlengi/fastapi_fizzbuzz/blob/main/docs_images/docs.png)

- To retrieve detail of FizzBuzz object from Api request, use `GET` http Method.
- `GET(Retrieve)` endpoint `http://127.0.0.1:8000/fizzbuzz/1`
- ![GET RETRIEVE API](https://github.com/Mhlengi/fastapi_fizzbuzz/blob/master
  /GETAllScreenshot.png)

### Running pytest
- Run `pytest app/tests.py`.

## Build the Docker Image
- Build your FastAPI image: `docker build -t app_image .`

## Start the Docker Container
- Run a container based on your image: `docker run -d --name mycontainer -p 80:80 app_image`
