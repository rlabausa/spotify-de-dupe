#!/path/to/python3/virtual/env

import json 

import requests

authorization_token = '<YOUR-AUTHORIZATION-TOKEN>'

headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {authorization_token}'
} 

# build request url
BASE_URL = 'https://api.spotify.com/v1' 
playlist_id = '<YOUR-PLAYLIST-ID>'
endpoint = f'playlists/{playlist_id}/tracks'
url = f'{BASE_URL}/{endpoint}'

# set parameters to be sent with the request
params = {'limit':100, 'fields':'(items(track(id, name, uri))), total, next'} 

# set to keep track of the song URIs we've already seen
existing_uris = set()

# array to store the state of the page objects
page_objs = []

next_url = url
while(next_url != None):
    req = requests.get(next_url, headers=headers, params=params)
    
    res = req.json()
    page_objs.append(res)

    next_url = res['next']

index = 0
next_url = f'{BASE_URL}/{endpoint}'

# go through page objects and delete duplicate tracks
for obj in page_objs:
    
    items = obj['items']

    for item in items:
        track = item['track']
        print(index, track)

        if track['uri'] in existing_uris:
            payload = {"tracks":[{"uri":track["uri"], "positions":[index]}]}
            payload = json.dumps(payload)

            del_req = requests.delete(next_url, headers=headers, data=payload)

            if del_req.status_code != 200:
                print(del_req.status_code, del_req.content)
            else:
                index -= 1
                print('DELETE', f'[{del_req.status_code}]', track['name'])
        
        else:
            existing_uris.add(track['uri'])
        
        index += 1
    
    next_url = obj['next']
    



