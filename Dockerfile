FROM python:3

WORKDIR /app

COPY . .

CMD ["python3","unit_test.py"]