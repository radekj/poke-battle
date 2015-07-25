from nameko.rpc import rpc, RpcProxy


class ScoreService(object):
    name = 'score_service'

    player_service = RpcProxy('players_service')

    @rpc
    def leaderboard(self):
        players = self.player_service.get_players()
        return sorted(players, key=lambda player: player.score, reverse=True)
