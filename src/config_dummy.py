from sqlalchemy import create_engine
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import discogs_client

mysql_connection=''
discogs_token=''
client_id = ''
client_secret = '' 
genres_html = ''
spotify_market=''

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
d = discogs_client.Client('my_user_agent/1.0', user_token=discogs_token)
engine = create_engine(mysql_connection)

