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

def get_apex_crafting_rotation():
    url = 'https://api.mozambiquehe.re/crafting?auth=ef056220ecc9350dd1214b2213643c87'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        daily_first_item = str(data[0]['bundleContent'][0]['itemType']['name']).capitalize().replace("_", " ")
        daily_first_item_rarity = str(data[0]['bundleContent'][0]['itemType']['rarity'])
        daily_second_item = str(data[0]['bundleContent'][1]['itemType']['name']).capitalize().replace("_", " ")
        daily_second_item_rarity = str(data[0]['bundleContent'][1]['itemType']['rarity'])
        weekly_first_item = str(data[1]['bundleContent'][0]['itemType']['name']).capitalize().replace("_", " ")
        weekly_first_item_rarity = str(data[1]['bundleContent'][0]['itemType']['rarity'])
        weekly_second_item = str(data[1]['bundleContent'][1]['itemType']['name']).capitalize().replace("_", " ")
        weekly_second_item_rarity = str(data[1]['bundleContent'][1]['itemType']['rarity'])
        first_weapon = str(data[2]['bundleContent'][0]['itemType']['name']).capitalize().replace("_", " ")
        second_weapon = str(data[3]['bundleContent'][0]['itemType']['name']).capitalize().replace("_", " ")

        response = [daily_first_item, daily_first_item_rarity, daily_second_item, daily_second_item_rarity, weekly_first_item,
                    weekly_first_item_rarity, weekly_second_item, weekly_second_item_rarity, first_weapon, second_weapon]
        
        return response

def get_player_level(player):
    url = f'https://api.mozambiquehe.re/bridge?auth=ef056220ecc9350dd1214b2213643c87&player={player}&platform=PC'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            level = data['global']['level']
        except KeyError:
            return 'DNE'
        
        return level


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
            await message.channel.send(f'The current map is {current_map} with {time_remaining} minutes remaining.\nNext map: {next_map}.')
            return
        if user_message.lower() == '!apexcraft':
            res = get_apex_crafting_rotation()
            await message.channel.send(f'Daily: {res[0]} ({res[1]}), {res[2]} ({res[3]})\nWeekly: {res[4]} ({res[5]}), {res[6]} ({res[7]})\nWeapons: {res[8]} and the {res[9]}.')
            return
        if '!apexlevel ' in user_message.lower():
            arr = user_message.lower().split()
            res = get_player_level(arr[1])
            if res != 'DNE':
                await message.channel.send(f'{arr[1]} is currently level {res}.')
            else:
                await message.channel.send(f'The player {arr[1]} does not exist. Please make sure to use their Origin account name.')
            return 

client.run(DISCORD_TOKEN)
