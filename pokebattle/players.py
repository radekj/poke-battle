from nameko.rpc import rpc
from nameko_sqlalchemy import Session
from sqlalchemy.ext.declarative import declarative_base 

from pokebattle.db import Player


Base = declarative_base()



class PlayersService(object):
    name = "players_service"
    session = Session(Base)

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
    def get_players(self):
        return self.session.query(Player).all()

    @rpc
    def get_player(self, uuid):
        return self.session.query(Player).filter(Player.id == uuid).first()

    def _check_name_duplicity(self, check_name):
        player = self.session.query(
            Player).filter(Player.name == check_name).first()
        if player:
            raise RuntimeError('The name of player already exists.')
