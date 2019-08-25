# app.py
from sanic import Sanic
from sanic.response import json, text, html
from api import api

app = Sanic(__name__)

app.blueprint(api) # Trong api có rất nhiều blueprint khác nhau


@app.route('/')
async def index(request):
    return html('<h1>Demo BluePrint</h1>'
                '<ul><li><a href="/api/post">/api/post</li>'
                '<li><a href="/api/songs">/api/songs</li>'
                '<li><a href="/api/post/template">/api/post/template</li>'
                '<li><a href="/api/content/">/api/content/</li>'
                '<li><a href="/api/content/authors">/api/content/authors</li>'
                '<li><a href="/api/content/authors/ferrario">/api/content/authors/ferrario</li> '
                '</ul>')

app.run(host="0.0.0.0", port=8000)
