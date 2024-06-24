from python:3.11-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /flask-app

CMD [ "python3", "run.py" ]