FROM debian

MAINTAINER Rick Greaves "rgreaves@google.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

COPY /code /app

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "index.py"]
