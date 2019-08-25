from sanic.response import json, text, html
from sanic import Blueprint
from jinja2 import Environment, FileSystemLoader
import os

current_path = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(current_path + "/templates"))

posts = Blueprint('posts', url_prefix='/post')


@posts.route('/')
async def posts_root(request):
    return json(
        [{
            "id": 1,
            "title": "Creator"
        }, {
            "id": 2,
            "title": "Go Now"
        }, {
            "id": 3,
            "title": "Peaceful Warrior"
        }, {
            "id": 4,
            "title": "Gamera vs. Guiron"
        }, {
            "id": 5,
            "title": "Idiot Box"
        }]
    )


@posts.route('/template')
async def posts_template(request):

    template = env.get_template('hello.html')
    content = template.render(title='Sanic', people='David')
    return html(content)