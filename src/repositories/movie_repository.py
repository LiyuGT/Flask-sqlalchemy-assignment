from src.models import Movie
from src.models import db

class MovieRepository:

    def get_all_movies(self, title) -> list[Movie]:
        # TODO get all movies from the DB
        movie: list[Movie]=Movie.query.all()
        return movie

    def get_movie_by_id(self, movie_id: int) -> Movie:
        # TODO get a single movie from the DB using the ID
        movie: Movie =Movie.query.first()
        return movie


    def create_movie(self, title: str, director: str, rating: int) -> Movie:
        # TODO create a new movie in the DB
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title: str) -> list[Movie]:
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movie: list[Movie] = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
        return movie


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
