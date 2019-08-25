from sanic import Sanic
from sanic.response import html

from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('1_load_from_template', 'templates'))

app = Sanic(__name__)


@app.route('/')
async def test(request):
    data = {'name': 'Trịnh Minh Cường'}

    template = env.get_template('index.html')  # Load index.html từ thư mục templates
    html_content = template.render(name=data["name"])
    return html(html_content)


app.run(host="0.0.0.0", port=8000)
