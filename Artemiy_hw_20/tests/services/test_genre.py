import pytest
from unittest.mock import MagicMock
from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService
from setup_db import db

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    trash = Genre(id=1, name="Trash")
    history = Genre(id=2, name="Histiry")
    science = Genre(id=3, name="Scince")

    genre_dao.get_one = MagicMock(return_value=trash)
    genre_dao.get_all = MagicMock(return_value=[trash, history, science])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao

class TestGenre:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0

    def test_create(self):
        genre1 = {"name": "Fantasy"}
        genre = self.genre_service.create(genre1)
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_upt = {"id": 3, "name": "SciFantastic"}
        self.genre_service.update(genre_upt)
