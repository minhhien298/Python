Demo một ứng dụng phức tạp sử dụng BluePrint để chia nhỏ các chức năng một web
site.


Trong mỗi thư mục cần có file __init__.py để import gom nhóm các BluePrint khác
```python
from sanic import Blueprint

from .posts import posts
from .content import content
from .songs import songs

api = Blueprint.group(posts, songs, content, url_prefix='/api')
``` 


Kinh nghiệm cho thấy sử dụng các module sanic_jinja... đều không xử lý tốt với
cấu trúc folder phức tạp

Sử dụng chiêu thức này để tìm ra đường dẫn đến thư mục chưa template cho jinja2

```python
import os

current_path = os.path.dirname(os.path.realpath(__file__))
env = Environment(loader=FileSystemLoader(current_path + "/templates"))
```



