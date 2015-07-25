
import unittest
from unittest.mock import Mock

from pokebattle.players import PlayersService, Player

class TestPlayers(unittest.TestCase):
    def test_new_player(self):
        test_name = 'Paul'
        new_player = PlayersService().new_player(test_name)
        self.assertIsInstance(new_player, Player)
        self.assertEquals(new_player.name, test_name)

    def test_get_pokemons(self):
        players_service = PlayersService()
        current_players = [players_service.new_player('John'), players_service.new_player('Mike')]
        self.assertEquals(current_players, players_service.get_players())

    def test_players_pokemons(self):
        players_service = PlayersService()
        player = players_service.new_player('Alex')
        pokemon_list = [Mock(), Mock()]
        for pokemon in pokemon_list:
            players_service.add_pokemon_to_player(player, pokemon)
        self.assertEquals(players_service.get_pokemons(player), pokemon_list)



if __name__ == '__main__':
    unittest.main()
