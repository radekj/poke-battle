from nameko.rpc import rpc, RpcProxy


class ScoreService(object):
    name = 'score_service'

    player_service = RpcProxy('players_service')

    @rpc
    def leaderboard(self):
        players = self.player_service.players()
        player_scores = [(player.name, player.score) for player in players]
        return sorted(player_scores, key=lambda player: player[1], reverse=True)
