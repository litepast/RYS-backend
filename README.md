# RYS Backend

This repository is the backend logic for the complete application, [the RYS frontend repository](https://github.com/litepast/rys-frontend) hosts the frontend logic, for which I used Vue.Js as the framework to build the graphical experience, logic and more!.

RYS (an acronym for Rate Your Spotify) is a personal project where you can add metadata of albums from Spotify on a personal database, so you can rate, play and edit them! Basically, a Spotify web player where you can add albums to your library, you will need to add the albums to your library in order to:

* Play the albums
* Rate the albums and its songs
* Edit some data that Spotify might not get right, such as genres or type of release 
* Get insight about your ratings, such as your favorite artists, years, decades and genres gieven your ratings via some dashboards

The reason for needing to add albums to your library in order to do the things above, is because this is not meant to substitute the Spotify core experience, but to have a database where you can have a sort of digital library with your ratings and such.

The idea behind this is heavily inspired by the site [rate your music](www.rateyourmusic.com) (now you know my project's name is not original!), where you can give music album ratings, but you cannot listen to them. The site is great enough for it to link you to sites where you can listen to music via links to spotify, Apple music and so on, but I wanted a sort of mix between the two where you can rate and play the songs on the same web app! Spotify as of this moment (November 2023) doesn't have the feature to give a numerical rating to albums or tracks, as it focuses on giving you recommendations given your listening habits.

This repository contains the backend logic, for which I created a RESTful API, build with Flask on Python. This connects to the [Spotify Web Api](https://developer.spotify.com/documentation/web-api) using a Python library [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/), which feeds the data to the frontend.

The Spotify Web API, sadly, is not great for the genres or subgenres of albums, it has the genres on the Artist metadata, so let's say if Artist X has one clearly rock album and another clearly electronic album, for spotify all albums are rock AND electronic if those genres are on the Artist X metadata.

As this project is focused on albums, my solution was to use the [Discogs](https://www.discogs.com/) API. Discogs is a online music database, where the genres and subgenres(called styles on it, so I stuck with it) are defined on each album, the definition is not the best in my opinion, but it is good enough, I'd have liked to use rateyourmusic.com but as of today (November 2023), it doesn't have an API and it doesn't allow webscrapping either. 

The database is built using [MySQL](https://www.mysql.com/), and the operations are all on python using [SQLAlchemy](https://www.sqlalchemy.org/), which connects to the MySQL database.

This includes a [dash dashboard](https://plotly.com/dash/), using its open source version. It allowed me to build Dashboard using just python, it creates an open-source alternative to tools such as Power Bi or Tableau.

## How to use this Project

You will need a Python enviroment on your systems if that was not clear enough! with PIP and all that comes with it, this project was built using Python 3.11. I used [VSCode](https://code.visualstudio.com/)  as IDE.

### Set up the database

[Install MySQL on your respective OS](https://dev.mysql.com/doc/refman/8.2/en/installing.html), then run the rys_schema.sql file on the mysql_files folder in order to create the RYS database

### Install the Python libraries

On the folder, run the next command to install the libraries used in this repository,
```sh
pip install -r requirements. txt
```


### Set up the config.py file

This might be the tickiest part, you will need the folliwing first

*
*


### Initialize the genres and styles tables on the database 
### Start the Flask Api


### Set up the Dash Dashboard
### Create CSV files for Tableau Dashboard (Optional)


## Credits
