from nameko.rpc import rpc, RpcProxy
from nameko_sqlalchemy import Session

from sqlalchemy.ext.declarative import declarative_base

from db import Pokemon

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
        pokemon = self.session.query(Pokemon).filter(
            Pokemon.id == pokemon_id
        ).first()
        if pokemon is None:
            return "Pokemon with id: {} doesn't exists".format(pokemon_id)
        return pokemon

    @rpc
    def get_pokemons_for_user(self, user_id):
        pokemon = self.session.query(Pokemon).filter(
            Pokemon.user_id == user_id
        ).first()
        if pokemon is None:
            return "User: {} doesn't have any pokemons assigned".format(user_id)
        return pokemon
