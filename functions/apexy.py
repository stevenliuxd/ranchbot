import requests

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

        response = [daily_first_item, daily_first_item_rarity, daily_second_item, daily_second_item_rarity, weekly_first_item,
                    weekly_first_item_rarity, weekly_second_item, weekly_second_item_rarity]
        
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