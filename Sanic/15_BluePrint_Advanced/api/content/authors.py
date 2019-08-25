# api/content/authors.py
from sanic import Blueprint
from sanic.response import json, text, html

authors = Blueprint('content_authors', url_prefix='/authors')


@authors.route("/")
async def info(request):
    return json(
        [{
            "id": 1,
            "first_name": "Nicol",
            "last_name": "Drescher"
        }, {
            "id": 2,
            "first_name": "Urbain",
            "last_name": "Snelson"
        }, {
            "id": 3,
            "first_name": "Abagail",
            "last_name": "Fazzioli"
        }, {
            "id": 4,
            "first_name": "Benoite",
            "last_name": "Exrol"
        }, {
            "id": 5,
            "first_name": "Leigha",
            "last_name": "Tute"
        }, {
            "id": 6,
            "first_name": "Rayna",
            "last_name": "Aikin"
        }, {
            "id": 7,
            "first_name": "Stephanie",
            "last_name": "O'Keaveny"
        }, {
            "id": 8,
            "first_name": "Therine",
            "last_name": "Meadley"
        }, {
            "id": 9,
            "first_name": "Maddie",
            "last_name": "Clement"
        }, {
            "id": 10,
            "first_name": "Ki",
            "last_name": "Breyt"
        }]
    )


@authors.route("/ferrario")
async def ferrario(request):
    return html("<h1>Ferrario</h1><img src='../static/ferrario.jpg'>")