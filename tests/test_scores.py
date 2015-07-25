import mock
from nameko.containers import ServiceContainer
from nameko.testing.services import worker_factory
from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter

from pokebattle.scores import ScoreService


def scores_service_with_players():
    players = [
        mock.MagicMock(name='player2', score=10),
        mock.MagicMock(name='player1', score=20)]
    service = worker_factory(ScoreService)
    service.player_rpc.get_players.side_effect = lambda: players
    service.player_rpc.get_player.side_effect = lambda p: players[p - 1]
    return service


def test_leaderboard():
    service = scores_service_with_players()
    leaderboard = service.leaderboard()
    assert leaderboard[0] == (service.player_rpc.get_players()[1].name, 20)
    assert leaderboard[1] == (service.player_rpc.get_players()[0].name, 10)


def test_empty_leaderboard():
    service = worker_factory(ScoreService)
    assert service.leaderboard() == []


def test_update_scores_on_battle_finished():
    service = scores_service_with_players()
    service.update_players_score([0, 1, 2])
    service.player_rpc.get_player(1).add_score.assert_called_once_with(2)
    service.player_rpc.get_player(2).add_score.assert_called_once_with(1)


def test_update_is_called_when_battle_finishes(rabbit_config):
    container = ServiceContainer(ScoreService, rabbit_config)
    container.start()

    dispatch = event_dispatcher(rabbit_config)

    with mock.patch.object(ScoreService, 'update_players_score') as mock_method:
        with entrypoint_waiter(container, 'update_players_score'):
            dispatch('battle_service', 'battle_finished', [0, 1, 2])
        mock_method.assert_called_once_with([0, 1, 2])

    container.stop()
