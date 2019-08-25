from sanic import Sanic
from sanic import response

app = Sanic()


@app.route("/")
async def homepage(request):
    return response.html("<h1>Hello World!</h1>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
