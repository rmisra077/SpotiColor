import requests
from getdominantcolor import get_major_color
import urllib.request

TOKEN_FILENAME = '../spotify_token.txt' # IMPORTANT! Replace this with where your Spotify token is stored

with open(TOKEN_FILENAME) as f: 
    lines = f.readlines()
token = lines[0]

currplayingurl = 'https://api.spotify.com/v1/me/player/currently-playing?market=ES'
headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def current_playing_color():
    r = requests.get(currplayingurl, headers=headers)
    print("Spotify Response:",r)
    
    r = r.json()
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