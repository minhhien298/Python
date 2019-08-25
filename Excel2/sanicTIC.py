from sanic import Sanic
from sanic import response

app = Sanic()


@app.route("/")
async def homepage(request):
    return response.text("Hello World!")

if __name__ == "__main__":
    app.run(host="192.168.13.103", port=8000)