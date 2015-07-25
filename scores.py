from nameko.rpc import rpc, RpcProxy
from nameko.events import event_handler

class ScoreService(object):
    name = 'score_service'

    player_rpc = RpcProxy('players_service')

    @rpc
    def leaderboard(self):
        players = self.player_rpc.get_players()
        sorted_players = sorted(players, key=lambda player: player.score, reverse=True)
        return [(p.name, p.score) for p in players]

    @event_handler('battle_service', 'battle_finished')
    def update_players_score(self, data):
        # NOTE: for now the winner gets 2 points and the loser 1
        _, winner, loser = data
        self.player_rpc.get_player(winner).add_score(2)
        self.player_rpc.get_player(loser).add_score(1)
