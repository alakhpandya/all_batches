FROM python:3.10-slim
WORKDIR /flask-docker

# RUN python.exe -m pip install --upgrade pip
# COPY requirements.txt /flask-docker/req.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "app.py"]

# Terminal command to run this file: docker build -t cars24 .
# Terminal command to run image file after above command: docker run -p 8000:5000 -d cars24