# spotify-de-dupe
Given a Spotify playlist ID and an access token with `playlist-modify-public`, `playlist-modify-private`, and `playlist-read-private` scope authorization, this script will remove all duplicate tracks from the specified Spotify playlist.

## Running Locally
1. Clone the repo
2. Install all required dependencies by running:
    ```
    pip3 install -r requirements.txt
    ```
3. Create a **.env** file in the root of the project directory and add `AUTH_TOKEN` and `PLAYLIST_ID` variables to it with your information. 
    - An example of a **.env** file is included in the repo. 
    - Your Spotify playlist ID can be found by clicking **Share > Copy Spotify URI** on any of your Spotify playlists (the URI will be the string of characters found after **spotify:playlist:**). 

4. Run the script with:
    ```
    python3 de_dupe.py
    ```
