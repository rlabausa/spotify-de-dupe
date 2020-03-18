#!/path/to/python3/virtual/env

import os
import json 

import requests
from dotenv import load_dotenv

PROJ_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(PROJ_DIR, '.env')
load_dotenv(ENV_PATH)

AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : f'Bearer {AUTH_TOKEN}'
} 

# build request url
BASE_URL = 'https://api.spotify.com/v1' 
PLAYLIST_ID = os.environ.get('PLAYLIST_ID')
ENDPOINT = f'playlists/{PLAYLIST_ID}/tracks'

url = f'{BASE_URL}/{ENDPOINT}'

# set parameters to be sent with the request
params = {'limit':100, 'fields':'(items(track(id, name, uri))), total, next'} 

def get_pages(reqURL, reqHeaders, reqParams):
    # keep track of the song URIs we've encountered
    existingURIs = set()

    # store the state of the page objects
    pages = []

    nextURL = reqURL
    while(nextURL != None):
        req = requests.get(nextURL, headers=reqHeaders, params=reqParams)
        
        res = req.json()
        pages.append(res)

        nextURL = res['next']
    
    return pages, existingURIs

def delete_dupes(pages, URIs, reqURL, reqHeaders):
    
    nextURL = reqURL
    index = 0
    
    for page in pages:
        
        items = page['items']

        for item in items:
            track = item['track']
            
            print(index, track)

            if track['uri'] in URIs:
                payload = {"tracks":[{"uri":track["uri"], "positions":[index]}]}
                payload = json.dumps(payload)

                deletedReq = requests.delete(nextURL, headers=reqHeaders, data=payload)

                if deletedReq.status_code != 200:
                    print(deletedReq.status_code, deletedReq.content)
                else:
                    index -= 1
                    print('DELETE', f'[{deletedReq.status_code}]', track['name'])
            
            else:
                URIs.add(track['uri'])
            
            index += 1
        
        nextURL = page['next']

pages, existingURIs = get_pages(url, headers, params)
delete_dupes(pages, existingURIs, url, headers, )

print('DONE')
    



