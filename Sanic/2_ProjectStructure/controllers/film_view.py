from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text


class FilmView(HTTPMethodView):
    def __init__(self, app, jinja):
        print("Film View Init")
        self.app = app
        self.jinja = jinja

    @app.route('/')
    async def get(self, request):
        return self.jinja.render_template("film.html", request)