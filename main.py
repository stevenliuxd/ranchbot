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

        daily_first_item = str(data[0]['bundleContent'][0]['itemType']['name']).capitalize()
        daily_first_item_rarity = str(data[0]['bundleContent'][0]['itemType']['rarity']).capitalize()

        daily_second_item = str(data[0]['bundleContent'][1]['itemType']['name']).capitalize()
        daily_second_item_rarity = str(data[0]['bundleContent'][1]['itemType']['rarity']).capitalize()

        weekly_first_item = str(data[1]['bundleContent'][0]['itemType']['name']).capitalize()
        weekly_first_item_rarity = str(data[1]['bundleContent'][0]['itemType']['rarity']).capitalize()

        weekly_second_item = str(data[1]['bundleContent'][1]['itemType']['name']).capitalize()
        weekly_second_item_rarity = str(data[1]['bundleContent'][1]['itemType']['rarity']).capitalize()

        first_weapon = str(data[2]['bundleContent'][0]['itemType']['name']).capitalize()
        second_weapon = str(data[3]['bundleContent'][0]['itemType']['name']).capitalize()

        response = [daily_first_item, daily_first_item_rarity, daily_second_item, daily_second_item_rarity, weekly_first_item,
                    weekly_first_item_rarity, weekly_second_item, weekly_second_item_rarity, first_weapon, second_weapon]
        
        return response

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
            [daily_first_item, daily_first_item_rarity, daily_second_item, daily_second_item_rarity, weekly_first_item,
            weekly_first_item_rarity, weekly_second_item, weekly_second_item_rarity, first_weapon, second_weapon] = get_apex_crafting_rotation()
            await message.channel.send(f'Today we are stocking the {daily_first_item_rarity} {daily_first_item} and \
                                       the {daily_second_item_rarity} {daily_second_item}.\n \
                                       This week, we have the {weekly_first_item_rarity} {weekly_first_item} as well as the \
                                       {weekly_second_item_rarity} {weekly_second_item}.\n \
                                       The weapons currently on rotation are the {first_weapon} and the {second_weapon}.')
            return


client.run(DISCORD_TOKEN)
