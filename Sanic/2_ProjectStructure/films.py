from sanic import Sanic
from sanic import response
from sanic_session import Session
from sanic_jinja2 import SanicJinja2

from controllers.film_view import *


app = Sanic()
Session(app)
jinja = SanicJinja2(app)


@app.route('/')
async def index(request):
    return response.html('<p>Films Web Site</p>')

app.add_route(FilmView(app, jinja).as_view(), '/film')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

