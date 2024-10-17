import requests
from decouple import config

MOZAM_API_TOKEN = config('MOZAM_API_KEY')

def get_apex_map():
    query_params = {'version': 2}

    url = f'https://api.mozambiquehe.re/maprotation?auth={MOZAM_API_TOKEN}'
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        data = response.json()

    br_current_map = data['battle_royale']['current']['map']
    br_time_remaining = data['battle_royale']['current']['remainingMins']
    br_next_map = data['battle_royale']['next']['map']

    ltm_current_mode = data['ltm']['current']['eventName']
    ltm_current_map = data['ltm']['current']['map']
    ltm_remaining = data['ltm']['current']['remainingMins']
    ltm_next_mode = data['ltm']['next']['eventName']
    ltm_next_map = data['ltm']['next']['map']

    br_resp = f'The current BR map is {br_current_map} with {br_time_remaining} minutes remaining. Next map: {br_next_map}.'
    ltm_resp = f'{ltm_current_mode} is playing on {ltm_current_map} with {ltm_remaining} minutes remaining. Next: {ltm_next_mode} on {ltm_next_map}.'

    return [br_resp, ltm_resp]

def get_apex_crafting_rotation():
    url = f'https://api.mozambiquehe.re/crafting?auth={MOZAM_API_TOKEN}'
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
    url = f'https://api.mozambiquehe.re/bridge?auth={MOZAM_API_TOKEN}&player={player}&platform=PC'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            level = data['global']['level']
        except KeyError:
            return 'DNE'
        
        return level
    