# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Movie(db.Model):

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
#class Movie:
    #def __init__(self, movie_id: int , title: str, director: str, rating: int) -> None:
        #self.movie_id = movie_id
        #self.title = title
        #self.director = director
        #self.rating = rating