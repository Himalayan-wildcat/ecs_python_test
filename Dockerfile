FROM python:3.7

WORKDIR /app

ENV FLASK_APP=main.py

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["python", "main.py"]
