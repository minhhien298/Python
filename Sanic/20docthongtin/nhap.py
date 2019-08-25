import pandas as pd
from sanic import Sanic
from sanic_session import Session
from sanic_jinja2 import SanicJinja2

df = pd.read_csv("friends.csv")
# df = pd.read_csv("OfficeSupplies.csv")
df.shape  # In ra kích thước dữ liệu (5000, 14) 5000 dòng, 14 cột
df.head(6)  # Trả dữ liệu mẫu, mặc định là 5 dòng đầu tiên
df.dtypes  # In ra kiểu dữ liệu từng cột
df.describe()
df.isnull().values.any() # Kiểm tra có cell nào bị null không?

app = Sanic()
Session(app)
jinja = SanicJinja2(app)
@app.route('/')
@jinja.template('index.html')  # decorator method is static method
async def index(request):
    return {'greetings': 'Hello, sanic!',
            'users': [{'name': df["name"],
                       'email': df["email"],
                       'mobile': df["mobile"]},

                      ]}

# Chú ý là file template luôn phải để trong thư mục templates
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)