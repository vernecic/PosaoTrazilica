FROM python:3.11

WORKDIR /app

COPY requirements.txt req.txt

RUN pip3 install -r req.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
