FROM python:3.9-slim
WORKDIR /app
ENV FLASK_APP=web
EXPOSE 8000

RUN apt update && apt upgrade
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "web:app"]
