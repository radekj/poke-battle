import pytest

from nameko.testing.services import worker_factory

from pokebattle.players import PlayersService


def test_players():
    players_service = worker_factory(PlayersService)

    first_name = 'Paul'
    first_player = players_service.new_player(first_name)
    players_service.new_player('Mike')

    assert first_player.name == first_name
    assert players_service.get_player(first_player.uuid).name == \
        first_player.name
    assert len(players_service.get_players()) == 2

    try:
        players_service.new_player(first_name)
        pytest.fail()
    except RuntimeError:
        pass
