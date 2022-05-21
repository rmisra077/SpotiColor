import requests
from getdominantcolor import get_major_color
import urllib.request



currplayingurl = 'https://api.spotify.com/v1/me/player/currently-playing?market=ES'
headers = {
    'Authorization': 'Bearer BQDLLHVAy9p2SZ1DyMsv23XhQHRKgGuuPms_tzB_1TpmuKvkxzblnj_uZ40C2V9nAYPVfyJI91QjvM2xYGFxUTGms4vljlqWjxWaKA77SLx7f2sZepJwT-8nUUbk8fHNJLNAvBcRxXdh5PMJPA',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def current_playing_color():

    r = requests.get(currplayingurl, headers=headers).json()
    # print(r)

    coverarturl = r['item']['album']['images'][1]['url']
    id = coverarturl.split('/')[-1]
    name = r['item']['name']

    # print()
    # print("Song:", name)
    # print("ID:", id)
    # print("Cover Art URL:", coverarturl)

    img_path = 'img/' + id + '.jpg'
    urllib.request.urlretrieve(coverarturl, img_path)



    # print("Color:", get_major_color(img_path))

    color = get_major_color(img_path)

    return color

    # print()