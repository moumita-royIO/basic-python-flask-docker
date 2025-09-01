FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY helper.py .

EXPOSE 5000

CMD ["python", "app.py"]