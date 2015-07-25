import unittest

from pokemon import PokemonService
from nameko.testing.services import worker_factory
from nameko_sqlalchemy import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestPokemon(unittest.TestCase):

    def setUp(self):
        self.session = Session(Base)

    def test_create_pokemon(self):
        service = worker_factory(PokemonService)
        service.create_pokemon(1, 'Bulbasaur')
