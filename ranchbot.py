import discord
from functions.apexy import get_apex_map, get_apex_crafting_rotation, get_player_level
from functions.weather import get_weather_by_city

DISCORD_TOKEN = "MTA4NDY1NTAzNjk2NzE2MjAwNg.GJTr6W.879A6HHZB69ImzRe8nbU6boZZg7xsIE1u7UKXA"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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
        if '!weather ' in user_message.lower():
            arr = user_message.lower().split()
            city_arr = arr[1:]
            city_string = ' '.join(str(element) for element in city_arr)
            res = get_weather_by_city(city_string)
            if res != 'DNE':
                await message.channel.send(res)
            else:
                await message.channel.send(f'Sorry, I failed to retrieve the data :(')
            return

client.run(DISCORD_TOKEN)
