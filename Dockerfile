FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/fogmlaas.py fogmlaas.py

#EXPOSE 9000

CMD ["python3", "/app/fogmlaas.py", "--port=9000"]
