from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import config

#engine = create_engine(config.mysql_connection)
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