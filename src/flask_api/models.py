from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import config

# it creates the SQL Alchemy models used on the insert_album.py file and the mysql connection...
# ...basically used on all the api's files

engine = config.engine
Base = automap_base()
Base.prepare(autoload_with=engine)
rys_artist = Base.classes.artists
rys_albums = Base.classes.albums
rys_tracks = Base.classes.tracks
rys_genres = Base.classes.genres_by_album
rys_styles = Base.classes.styles_by_album
rys_album_ratings = Base.classes.album_ratings
rys_tracks_ratings = Base.classes.track_ratings