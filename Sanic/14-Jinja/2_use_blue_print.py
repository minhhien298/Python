from sanic import Sanic
from my_blueprint import bp # import my_blueprint.py

app = Sanic(__name__)
app.blueprint(bp)

app.run(host='0.0.0.0', port=8000, debug=True)