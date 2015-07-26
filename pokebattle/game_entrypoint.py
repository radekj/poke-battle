import json

from nameko.web.handlers import http
from nameko.rpc import RpcProxy

from pokebattle.scores import ScoreService


class GameService(object):
    name = 'game_service'
    score_rpc = RpcProxy('score_service')

    @http('POST', '/signup')
    def signup(self, request):
        pass

    @http('POST', '/login')
    def login(self, request):
        pass

    @http('POST', '/battle')
    def new_game(self, request):
        pass

    @http('GET', '/leaderboard')
    def leaderboard(self, request):
        return json.dumps(self.score_rpc.leaderboard())

    @http('GET', '/user/<int:id>')
    def user(self, request):
        pass

    @http('GET', '/user/<int:id>/pokemons')
    def user_pokemons(self, request):
        pass
