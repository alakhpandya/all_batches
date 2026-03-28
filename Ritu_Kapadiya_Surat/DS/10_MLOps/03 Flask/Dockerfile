FROM python:3.10-slim
WORKDIR /flask-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "app.py" ]

# Terminal command to build the image: docker build -t flaskapp .
# Terminal command to run image file after above command: docker run -p 8000:8000 -d flaskapp