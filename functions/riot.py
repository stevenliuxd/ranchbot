import requests

def get_riot_account_info(game_name, tag_line, api_key):
    base_url = "https://americas.api.riotgames.com"
    endpoint = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {
        "X-Riot-Token": api_key,
    }

    url = base_url + endpoint

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def get_tft_matchlist(puuid, api_key):
    base_url = "https://americas.api.riotgames.com"
    endpoint = f"/tft/match/v1/matches/by-puuid/{puuid}/ids"
    headers = {
        "X-Riot-Token": api_key,
    }

    url = base_url + endpoint

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
def get_tft_match(matchId, api_key):
    base_url = "https://americas.api.riotgames.com"
    endpoint = f"/tft/match/v1/matches/{matchId}"
    headers = {
        "X-Riot-Token": api_key,
    }

    url = base_url + endpoint

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
####################### TEST #########################

api_key = "RGAPI-30c2a42e-e2ea-42ec-ac33-72a32a944c49"
game_name = "ShnauzerR"  # Replace with the Riot ID game name
tag_line = "NA1"    # Replace with the Riot ID tag line

account_info = get_riot_account_info(game_name, tag_line, api_key)
puuid = str({account_info['puuid']}).replace("{", "").replace("}", "").replace("'", "")

matchlist = get_tft_matchlist(puuid, api_key)
print(matchlist)
print(get_tft_match(matchlist[0], api_key))
