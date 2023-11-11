import requests

def get_public_ip_address():
    response = requests.get('https://api64.ipify.org?format=json')
    res = response.json()['ip']
    ip_address = f'The public IP of this ranchbot host is: {res}'
    return ip_address
