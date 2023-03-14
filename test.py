import requests

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


