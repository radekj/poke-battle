from nameko.containers import ServiceContainer
from nameko.testing.services import worker_factory
from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter

from scores import ScoreService


def scores_service_with_players():
    service = worker_factory(ScoreService)
    service.player_rpc.new_player('player1')
    service.player_rpc.new_player('player2')
    service.player_rpc.get_player(1).add_score(10)
    service.player_rpc.get_player(2).add_score(20)
    return service

def test_leaderboard():
    service = scores_service_with_players()

    assert service.leaderboard() == [('player2', 20), ('player1', 10)]

def test_empty_leaderboard():
    service = worker_factory(ScoreService)
    assert service.leaderboard() == []

def test_update_scores_on_battle_finished():
    service = scores_service_with_players()
    winner = service.player_rpc.get_player(1)
    loser = service.player_rpc.get_player(2)
    service.update_players_score([0, 1, 2])
    assert service.player_rpc.get_player(1) == winner.score + 2
    assert service.player_rpc.get_player(2) == winner.score + 1

def test_update_is_called_when_battle_finishes(rabbit_config):
    container = ServiceContainer(ScoreService, rabbit_config)
    container.start()

    dispatch = event_dispatcher(rabbit_config)

    with entrypoint_waiter(container, 'update_players_score'):
        dispatch('battle_service', 'battle_finished', [0, 1, 2])

    # NOTE: not sure if this will work
    container.service_cls.update_players_score.assert_called_once_with([0, 1, 2])

    container.stop()
