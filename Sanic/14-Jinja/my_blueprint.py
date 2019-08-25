# more my_blueprint.py
from sanic.response import json, text, html
from sanic import Blueprint
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('my_blueprint', 'templates'))

bp = Blueprint('my_blueprint')


@bp.route('/')
async def bp_root(request):
    template = env.get_template('hello.html')
    content = template.render(title='Sanic', people='David')
    return html(content)
