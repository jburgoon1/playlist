"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__= "playlist"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = True)
    description = db.Column(db.String)


class Song(db.Model):
    """Song."""
    __tablename__ = "songs"
    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable = True)
    artist = db.Column(db.String, nullable = True)
    playlist = db.relationship("Playlist", backref = "songs", secondary = "playlists_songs")

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlists_songs"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('songs.id'))

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
