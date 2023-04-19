import pytest

from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService
from setup_db import db

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    kubrick = Director(id=1, name="Stanley Kubrick")
    trier = Director(id=2, name="Lars von Trier")
    baskova = Director(id=3, name="Svetlana Baskova")

    director_dao.get_one = MagicMock(return_value=kubrick)
    director_dao.get_all = MagicMock(return_value=[kubrick, trier, baskova])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirector:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        dir_1 = {"name": "Ivan Ivanov"}
        director = self.director_service.create(dir_1)
        assert director.id != None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        dir_upt = {"id": 3, "name": "Ivan Iv"}
        self.director_service.update(dir_upt)

