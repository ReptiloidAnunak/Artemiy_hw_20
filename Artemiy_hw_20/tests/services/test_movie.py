from unittest.mock import MagicMock
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db
import pytest


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    brat1 = Movie(id=1, title="title1", description="dwafan1", trailer="ютуб", year=1990, rating=1, genre=1, director=2)
    brat2 = Movie(id=2, title="title2", description="awda2", trailer="ютуб", year=1990, rating=2, genre=1, director=2)
    woodstock = Movie(id=3, title="title3", description="description3", trailer="ютуб", year=1990, rating=3, genre=1, director=2)

    movie_dao.get_one = MagicMock(return_value=brat1)
    movie_dao.get_all = MagicMock(return_value=[brat1, brat2, woodstock])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao

class TestMovie:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)


    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_zs = {"title": "Зеленый слоник", "description": "Фильм про армию", "trailer": "ютуб", "year": 1999, "rating": 10}
        movie = self.movie_service.create(movie_zs)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        brat3 = {"id": 1, "title": "Зеленый слоник", "description": "Фильм про армию", "trailer": "ютуб", "year": 1999, "rating": 10}
        self.movie_service.update(brat3)
