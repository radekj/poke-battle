from nameko.rpc import rpc, RpcProxy
from nameko_sqlalchemy import Session
from sqlalchemy.ext.declarative import declarative_base

from pokebattle.utils import dictify
from pokebattle.db import Player


Base = declarative_base()


class PlayersService(object):
    name = "players_service"
    session = Session(Base)

    pokemon_service = RpcProxy('pokemon_service')

    @rpc
    def new_player(self, name):
        """
        :param name: str Name of player
        """
        self._check_name_duplicity(name)
        player = Player(name=name)
        self.session.add(player)
        self.session.commit()
        return player

    @rpc
    @dictify
    def get_players(self):
        return self.session.query(Player).all()

    @rpc
    @dictify
    def get_player(self, uuid):
        return self.session.query(Player).filter(Player.id == uuid).first()

    def _check_name_duplicity(self, check_name):
        player = self.session.query(
            Player
        ).filter(Player.name == check_name).first()
        if player:
            raise RuntimeError('The name of player already exists.')

    @rpc
    def create_pokemon_for_player(self, uuid):
        self.pokemon_service.create_pokemon(uuid)

    @rpc
    def get_pokemons_for_player(self, uuid):
        return self.pokemon_service.get_pokemons_for_user(uuid)
