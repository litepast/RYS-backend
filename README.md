# RYS Backend

This repository is the backend logic for the complete application, [the RYS frontend repository](https://github.com/litepast/rys-frontend) hosts the frontend logic, for which I used Vue.Js as the framework to build the graphical experience, logic and more!.

RYS (acronym for Rate Your Spotify) is personal project where you can add metadata of albums from Spotify on a personal database, so you can rate, play and edit them! Basically a spotify web player where you can add albums to your library, you will need to add the albums to your library in order to:
* Play the albums
* Rate the albums and its songs
* Edit some data spotify might not get right such as genres or type of release 
* Get insight about your ratings such as your favorite artists, years, decades and genres gieven your ratings via some dahsboards

The reason for needing to add albums to your library in order to do the things above, is because this is not meant to substitute the Spotify core expetience, but to have database where you can have a sort of digital library with your ratings and such.

The idea behind this is heavily inspired by the site [rate your music](www.rateyourmusic.com) (now you know my project's name is not original!), where you can give music albume ratings, but you cannot listen to them, the site is great enough for it to link you to sites where you can listen to the music via links to spotify, apple music and so on, but I wanted a sort of mix between the two where you can rate and play the songs on the same web app! Spotify as of this moment (November 2023) doesn't have the feature to give a numerical rating to albums nor tracks as it focuses on giving you recommendations given your listening habbits.

This repository contains the backend logic, for which I created a RESTful API, build with Flask on Python, this connects to the [Spotify Web Api](https://developer.spotify.com/documentation/web-api) using a Python library [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/), which feeds the data to the frontend.

The Spotify Web API, sadly, is not great for the genres or subgenres of albums, it has the genres on the Artist metadata, so let's say if Artist X has one crearly rock album and another clearly electronic album, for spotify all albums are rock AND electronic if those genres are on the Artist X metadata.

As this project is focused on albums, amy solution was to use the [Discogs](https://www.discogs.com/) API, Discogs is a music online database, where the genres and subgenres(called styles on it, so I stuck with it) are defined on each album, the definition is not the best in my opinion, but it is good enough, I'd have liked to use rateyourmusic.com but as of today (November 2023), it doesn't have an API and it doesn't allow webscrapping either. 

The database is build using [MySQL](https://www.mysql.com/), and the operations are all on python using [SQLAlchemy](https://www.sqlalchemy.org/), which connects to the MySQL database.

This contains a [dash dashboard](https://plotly.com/dash/), using its open source version, it allowed me to build Dashboard using just python, a create open source alternative to tools such as Power Bi or Tableua.

## How to use this Project
### Set up the database
### Install the Python libraries
### Set up the config.py file
### Initialize the genres and styles tables on the database 
### Start the Flask Api
### Set up the Dash Dashboard
### Create CSV files for Tableau Dashboard (Optional)


## Credits
