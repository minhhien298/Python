from sanic import Sanic
from sanic_session import Session
from sanic_jinja2 import SanicJinja2

# pip install sanic_session
# pip install sanic_jinja2

app = Sanic()

Session(app)

jinja = SanicJinja2(app)


@app.route('/')
@jinja.template('index.html')  # decorator method is static method
async def index(request):
    return {'greetings': 'Hello, sanic!',
            'users': [{'url': 'https://vnexpress.net',
                       'username': 'Cuong'},
                      {'url': 'https://google.com',
                       'username': 'Sergey Bin'}
                      ]}

# Chú ý là file template luôn phải để trong thư mục templates

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)