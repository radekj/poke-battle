import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from nameko.testing.services import worker_factory

from pokebattle.db import Base
from pokebattle.pokemon import PokemonService


@pytest.fixture
def service(session):
    return worker_factory(PokemonService, session=session)


@pytest.fixture
def session():
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    session_cls = sessionmaker(bind=engine)
    session = session_cls()
    return session


def test_create_pokemon():
    service = worker_factory(PokemonService)
    service.create_pokemon(1, 'Bulbasaur')

    assert service.session.add.call_count == 1

    created_pokemon = service.session.add.call_args[0][0]
    assert created_pokemon.user_id == 1
    assert created_pokemon.pokemon_name == 'Bulbasaur'


def test_get_pokemon_by_id(service):
    service.create_pokemon(1, 'Bulbasaur')
    pokemon = service.get_pokemon_by_id(1)
    assert pokemon, (pokemon.id, 1, u'Bulbasaur')


def test_get_pokemon_by_id_none_found(service):
    pokemon = service.get_pokemon_by_id(999)
    assert pokemon is None


def test_get_pokemons_for_user(service):
    service.create_pokemon(1, 'Bulbasaur')
    pokemon = service.get_pokemons_for_user(1)
    assert pokemon, (pokemon.id, 1, u'Bulbasaur')


def test_get_pokemons_for_user_none_found(service):
    service.create_pokemon(1, 'Bulbasaur')
    pokemon = service.get_pokemons_for_user(999)
    assert pokemon is None
