# spotify-de-dupe
Given a Spotify playlist ID and an access token--with `playlist-modify-public`, `playlist-modify-private`, and `playlist-read-private` scope authorization--this script will go through the specified Spotify playlist and remove all duplicate tracks.

## Running Locally
Clone the repo, then install the required dependencies by running:
```
pip3 install -r requirements.txt
```
Before running the script, modify it with your `authorization_token` and `playlist_id`. Your playlist id can be found by clicking **Share > Copy Spotify URI** on your spotify playlist (the URI will be the string of characters found after **spotify:playlist:**) 

Then, execute the script with:
```
python3 de_dupe.py
```