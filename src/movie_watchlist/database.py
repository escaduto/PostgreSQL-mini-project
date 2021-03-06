import datetime 
import sqlite3

CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    title TEXT, 
    release_timestamp REAL, 
    watched INTEGER
)

"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES  = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"

connection = sqlite3.connect("data.db")

def create_tables():
    pass


def add_movie(title, release_timestamp):
    pass


def get_movies(upcoming=False):
    pass


def watch_movie(movie_title):
    pass


def get_watched_movies():
    pass