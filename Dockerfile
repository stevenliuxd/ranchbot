FROM ranchbot-base:latest

WORKDIR /app

COPY . .

CMD ["python", "ranchbot.py"]
