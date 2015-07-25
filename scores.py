from nameko.rpc import rpc, RpcProxy


class ScoreService(object):
    name = 'score_service'

    player_rpc = RpcProxy('players_service')

    @rpc
    def leaderboard(self):
        players = self.player_rpc.get_players()
        sorted_players = sorted(players, key=lambda player: player.score, reverse=True)
        return [(p.name, p.score) for p in players]

    @rpc
    def update_player_score(self, player_id, score):
        player = self.player_rpc.get_player(player_id)
        player.add_score(score)
