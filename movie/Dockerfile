FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY add.py .

EXPOSE 5001

CMD ["python", "add.py"]
