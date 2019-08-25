# api/content/__init__.py
from sanic import Blueprint
from sanic.response import json, text, html
from .authors import authors

import os
current_path = os.path.dirname(os.path.realpath(__file__))
bpStatic = Blueprint('static', url_prefix='/static')
bpStatic.static('/', current_path + '/static')

bpIndex = Blueprint('index', url_prefix='/')
@bpIndex.route('/')
async def index(request):
    return html("<h1>/content/</h1>")

content = Blueprint.group(bpIndex, authors, bpStatic, url_prefix='/content')
