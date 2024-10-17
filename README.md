# Ranchbot
Simple bot with many features!
Dedicated to the friends at Ni Hao Discord.

## How to use
Create a file ```.env``` in root dir and populate it with your API Keys.
```
DISCORD_API=yourdiscAPIhere
```

Build the docker container
```
docker build -t ranchbot .
```

Running the docker container
```
docker run --rm -it --env-file .env ranchbot
```
