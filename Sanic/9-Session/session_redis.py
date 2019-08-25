import asyncio_redis

from sanic import Sanic
from sanic.response import text
from sanic_session import Session, RedisSessionInterface

app = Sanic()


class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host='localhost', port=6379, poolsize=10
            )

        return self._pool


redis = Redis()

Session(app, interface=RedisSessionInterface(redis.get_redis_pool))


@app.route("/")
async def test(request):
    # interact with the session like a normal dict
    if not request['session'].get('foo'):
        request['session']['foo'] = 0

    request['session']['foo'] += 1

    response = text(request['session']['foo'])

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)