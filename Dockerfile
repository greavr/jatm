FROM python:3.7.3

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

COPY /code /app

WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "index.py"]
