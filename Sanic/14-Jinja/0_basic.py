from jinja2 import Template
from sanic import Sanic
from sanic.response import text

template = Template('Hello {{ name }}!')

app = Sanic()


@app.route("/")
async def test(request):
    return text(template.render(name="Cường"))

app.run(host="0.0.0.0", port=8000)