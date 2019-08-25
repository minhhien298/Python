from sanic import Sanic
from sanic import response
import asyncio
import ujson  # Thư viện json sử dụng C/C++ cực nhanh
app = Sanic()
#app.static('/static', './static')

# http://localhost:8000/12
@app.route("/<i:int>/<count:int>")
async def test(request, i, count):
    from_range = 0
    to_range = 0

    if count > 0:
        from_range = i
        to_range = i + count
    else:
        from_range = i + count
        to_range = i

    result = "["

    for k in range(from_range, to_range):
        result += f'{{"id": {k},"title": "Title {k}","subtitle": "Subtitle {k}", "photo": "{k:03}.jpg"}}'
        if k < to_range - 1:
            result += ","

    result += "]"
    await asyncio.sleep(2)
    return response.json(ujson.loads(result))


@app.route('/static/<photo>')
async def handle_request(request, photo):
    await asyncio.sleep(2)
    return await response.file_stream(f'./static/{photo}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
