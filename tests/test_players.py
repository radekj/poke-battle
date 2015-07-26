import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from nameko.testing.services import worker_factory

from pokebattle.db import Base
from pokebattle.players import PlayersService


@pytest.fixture
def session():
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    session_cls = sessionmaker(bind=engine)
    session = session_cls()
    return session


@pytest.fixture
def service(session):
    return worker_factory(PlayersService, session=session)


def test_players(service):
    first_name = 'Paul'
    first_player = service.new_player(first_name)
    service.new_player('Mike')

    assert first_player.name == first_name
    assert service.get_player(first_player.id)['name'] == \
        first_player.name
    assert len(service.get_players()) == 2

    try:
        service.new_player(first_name)
        pytest.fail()
    except RuntimeError:
        pass
