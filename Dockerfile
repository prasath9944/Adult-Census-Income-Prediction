FROM python:3.7-slim-buster
RUN apt update -y && apt install awscli -y
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python","app.py" ]