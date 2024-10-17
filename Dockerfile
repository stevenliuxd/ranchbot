FROM python:3.9-slim

WORKDIR /app

RUN pip install discord.py python-decouple requests

COPY . .

CMD ["python", "ranchbot.py"]
