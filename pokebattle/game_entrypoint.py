from nameko.web.handlers import http

from pokebattle.scores import ScoreService


class GameService(object):

    score_service = RpcProxy('score_service')

    @http('POST', '/signup')
    def signup(self):
        pass

    @http('POST', '/login')
    def login(self):
        pass

    @http('POST', '/battle')
    def new_game(self):
        pass

    @http('GET', '/leaderboard')
    def leaderboard(self):
        pass

    @http('GET', '/user/<int:id>')
    def user(self):
        pass

    @http('GET', '/user/<int:id>/pokemons')
    def user_pokemons(self):
        pass
