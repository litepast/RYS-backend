import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import discogs_client

mysql_connection='mysql+mysqlconnector://root:Adults2137224!@localhost:3306/rys'
client_id = '9a65d633d6cc467ea07bb013b29b4b6a'
discogs_token='uytzEONbTVeTThmGsfMAAdmjrvbSzYmMrohodPAE'
client_secret = '5de4eb24942449aeae4f0288247b2b5a'   
genres_html = 'C:/SideProjects/RateYourSpotify/backend/source/Genres/Genres_and_Styles_Discogs.html'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
d = discogs_client.Client('my_user_agent/1.0', user_token=discogs_token)