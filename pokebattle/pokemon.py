from nameko.rpc import rpc, RpcProxy
from nameko_sqlalchemy import Session
from sqlalchemy.ext.declarative import declarative_base

from pokebattle.db import Pokemon


Base = declarative_base()


class PokemonService(object):
    name = 'pokemon_service'
    session = Session(Base)

    player_service = RpcProxy('players_service')

    @rpc
    def create_pokemon(self, user_id, pokemon_name):
        # TODO: fetch pokemon's features from http://pokeapi.co
        pokemon = Pokemon(user_id=user_id, pokemon_name=pokemon_name)
        self.session.add(pokemon)
        self.session.commit()

    @rpc
    def get_pokemon_by_id(self, pokemon_id):
        return self.session.query(
            Pokemon.id,
            Pokemon.user_id,
            Pokemon.pokemon_name,
        ).filter(
            Pokemon.id == pokemon_id
        ).first()

    @rpc
    def get_pokemons_for_user(self, user_id):
        return self.session.query(
            Pokemon.id,
            Pokemon.user_id,
            Pokemon.pokemon_name,
        ).filter(
            Pokemon.user_id == user_id
        ).first()
