import discord
import requests

DISCORD_TOKEN = "MTA4NDY1NTAzNjk2NzE2MjAwNg.GYi6TN.Xi8aGzvvIn8lnys5L96zIYBKLXnIldh_X4zSY4"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_apex_map():
    query_params = {'version': 1}

    url = 'https://api.mozambiquehe.re/maprotation?auth=ef056220ecc9350dd1214b2213643c87'
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        data = response.json()

    current_map = data['battle_royale']['current']['map']
    time_remaining = data['battle_royale']['current']['remainingMins']
    next_map = data['battle_royale']['next']['map']

    return [current_map, time_remaining, next_map]

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'bots':
        if user_message.lower() == '!apexmap':
            [current_map, time_remaining, next_map] = get_apex_map()
            await message.channel.send(f'The current map is {current_map} with {time_remaining} minutes remaining.')
            await message.channel.send(f'Next map: {next_map}.')
            return

client.run(DISCORD_TOKEN)
