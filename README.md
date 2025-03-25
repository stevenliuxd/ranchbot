# Ranchbot
Simple bot with many features!
Dedicated to the friends at Ni Hao Discord.

## How to use
Create a file ```.env``` in root dir and populate it with your API Keys.
```
DISCORD_API=...
MOZAM_API_KEY=...
GEO_API_KEY=...
WEATHER_API_KEY=...
```

Build the docker container
```
docker build -f Dockerfile.base -t ranchbot-base:latest .
docker build -t ranchbot .
```

Running the App
```
docker run --rm -it --env-file .env ranchbot
```

Note: To automate this, create a systemd service that runs the above command along with the env file.
```
ExecStart=/usr/bin/docker run --rm --env-file /home/steven/code/ranchbot/.env ranchbot
```

## Run in Kubernetes
This is super uneccesary; we're doing this because we can. 

Make sure minikube is installed & running on the host, and create the following secrets:
```
kubectl create secret generic discord-api-key --from-literal=DISCORD_API_KEY=your_discord_api_key
kubectl create secret generic geo-api-key --from-literal=GEO_API_KEY=your_geo_api_key
kubectl create secret generic mozam-api-key --from-literal=MOZAM_API_KEY=your_mozam_api_key
kubectl create secret generic weather-api-key --from-literal=WEATHER_API_KEY=your_weather_api_key
```

Apply the terraform config (main.tf).
