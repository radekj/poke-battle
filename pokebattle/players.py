from nameko.rpc import rpc

class PlayersService(object):
    name = "players_service"

    _players = []

    @rpc
    def new_player(self, name: str):
        new_player = Player(name)
        self._players.append(new_player)
        return new_player

    @rpc
    def get_players(self):
        return self._players

    @rpc
    def add_pokemon_to_player(self, player, pokemon):
        player.add_pokemon(pokemon)

    @rpc
    def get_pokemons(self, player):
        return player.get_pokemons()


class Player(object):
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self._pokemons = []

    def add_score(self, points_from_battle):
        self.score += points_from_battle

    def add_pokemon(self, pokemon):
        self._pokemons.append(pokemon)

    def get_pokemons(self):
        return self._pokemons
