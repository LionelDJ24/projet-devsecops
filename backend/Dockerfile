FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY . .
# On tourne en root (vulnérabilité volontaire)
CMD ["python", "app.py"]
