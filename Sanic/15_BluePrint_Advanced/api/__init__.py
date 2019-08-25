from sanic import Blueprint

from .posts import posts
from .content import content
from .songs import songs

api = Blueprint.group(posts, songs, content, url_prefix='/api')