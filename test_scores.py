from scores import ScoreService
from nameko.testing.services import worker_factory


class TestScores(unittest.TestCase):
    def test_leaderboard(self):
        service = worker_factory(ScoreService)
        service.player_rpc.new_player('player1')
        service.player_rpc.new_player('player2')
        service.player_rpc.get_player(1).add_score(10)
        service.player_rpc.get_player(2).add_score(20)

        self.assertEquals(
            service.leaderboard(),
            [('player2', 20), ('player1', 10)])

    def test_empty_leaderboard(self):
        service = worker_factory(ScoreService)
        self.assertEquals(service.leaderboard(), [])
