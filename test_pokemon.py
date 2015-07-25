import unittest

from pokemon import PokemonService
from nameko.testing.services import worker_factory


class TestPokemon(unittest.TestCase):

    def setUp(self):
        self.service = worker_factory(PokemonService)

    def test_create_pokemon(self):
        self.service.create_pokemon(1, 'Bulbasaur')

        self.assertEqual(self.service.session.add.call_count, 1)

        created_pokemon = self.service.session.add.call_args[0][0]
        self.assertEqual(created_pokemon.user_id, 1)
        self.assertEqual(created_pokemon.pokemon_name, 'Bulbasaur')

    def get_pokemon_by_id():
        pass
