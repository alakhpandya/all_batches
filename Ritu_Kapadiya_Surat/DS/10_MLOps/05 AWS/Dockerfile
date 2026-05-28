FROM python:3.10-slim
WORKDIR /flask-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "app.py" ]
# python app.py

# Two important commands:
    # 1. To build a docker image: docker build -t docker_test .
    # 2. To run the docker image: docker run -p 8000:8000 -d docker_test