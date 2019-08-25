from sanic.response import json, text, html
from sanic import Blueprint
from jinja2 import Environment, FileSystemLoader
import os

current_path = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(current_path + "/templates"))

songs = Blueprint('songs', url_prefix='/songs')


@songs.route('/')
async def index(request):
    template = env.get_template('songs.html')
    data = [
    {
      "id": 1,
      "title": "Calling, The"
    }, {
      "id": 2,
      "title": "Nasty Girl, The (schreckliche Mädchen, Das)"
    }, {
      "id": 3,
      "title": "Miss Farkku-Suomi"
    }, {
      "id": 4,
      "title": "House of D"
    }, {
      "id": 5,
      "title": "Blind Justice (Hævnens nat)"
    }, {
      "id": 6,
      "title": "13 Beloved (13 game sayawng)"
    }, {
      "id": 7,
      "title": "Chris Rock: Bigger & Blacker"
    }, {
      "id": 8,
      "title": "Cinema Verite"
    }, {
      "id": 9,
      "title": "Blade on the Feather (Deep Cover)"
    }, {
      "id": 10,
      "title": "Am Ende eiens viel zu kurzen Tages (Death of a superhero)"
    }]
    return html(template.render(songs=data))
