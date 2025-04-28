FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web_scraper.py .

CMD ["python", "web_scraper.py"]