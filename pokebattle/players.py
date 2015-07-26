from nameko.rpc import rpc


class PlayersService(object):
    name = "players_service"

    _players = {}

    @rpc
    def new_player(self, name):
        """
        :param name: str Name of player
        """
        self._check_name_duplicity(name)
        new_player = Player(name)
        self._players[new_player.uuid] = new_player
        return new_player

    @rpc
    def get_players(self):
        return [player for player in self._players]

    @rpc
    def get_player(self, uuid):
        return self._players[uuid]

    def _check_name_duplicity(self, check_name):
        for player in self._players.values():
            if check_name == player.name:
                raise RuntimeError('The name of player already exists.')


class Player(object):
    # counter for autoincrement
    counter = 0

    def __init__(self, name):
        """
        :param name: str
        """
        self.name = name
        self.score = 0
        Player.counter += 1
        self.uuid = Player.counter

    def add_score(self, points_from_battle):
        self.score += points_from_battle
