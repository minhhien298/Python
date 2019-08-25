# Render templates in a Flask like way from a "template" directory in
# the project

from sanic import Sanic
from sanic import response
from jinja2 import Environment, PackageLoader, select_autoescape

import sys
# Enabling async template execution which allows you to take advantage
# of newer Python features requires Python 3.6 or later.
enable_async = sys.version_info >= (3, 6)


app = Sanic(__name__)

# Load the template environment with async support
template_env = Environment(
    loader=PackageLoader('3_async_template', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=enable_async
)

# Load the template from file
template = template_env.get_template("example_template.html")


@app.route('/')
async def test(request):
    # Sử dụng async không tăng tốc lên so với sync
    rendered_template = await template.render_async(
        knights='that say nih; asynchronously')
    return response.html(rendered_template)

    # Không sử dụng async
    #return response.html(template.render(knights='that say nih; asynchronously'))

app.run(host="0.0.0.0", port=8000, debug=False)

'''
@patic-fr Reading template files in async is just a bad idea, this should be done once during program startup and then they should be kept cached in memory. Reading them every time you serve a request is just wasteful.

Spawning a coroutine for rendering is another bad idea, rendering your templates is inherently CPU bound and will put pressure on your event loop no matter where they are, there is nothing to be gained by rendering them asynchronously.

In short: Stop reading the file every time, don't render in a separate async function.
'''
