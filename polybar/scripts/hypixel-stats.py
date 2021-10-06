import json
import requests
import math

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

API_KEY = "566532b7-d0b1-426b-9a5f-e9705b50847d"
UUID = "22635ba6-244d-422d-a407-7002f33b2109"

hypixel_data = requests.get("https://api.hypixel.net/player?key=" + API_KEY + "&uuid=" + UUID ).json()
network_experience = hypixel_data["player"]["networkExp"]
network_level = (math.sqrt((2 * network_experience) + 30625) / 50) - 2.5
#network_level = round(network_level, 2)
network_level = math.trunc(network_level)

skywars_kills = hypixel_data["player"]["stats"]["SkyWars"]["kills"] 
skywars_wins = hypixel_data["player"]["stats"]["SkyWars"]["wins"] 

#print ("Network level: " + network_level)
print (" {0}  - {1}  - {2}  ".format(network_level, skywars_kills, skywars_wins))
