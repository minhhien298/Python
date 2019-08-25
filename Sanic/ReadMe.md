Sanic chạy gần như nhanh nhất trong các Python framework. Chậm hơn Golang Iris khoảng 4 lần
Sanic chạy nhanh tương đương với Node.js Express

Để xem process nào đang lắng nghe ở một cổng trên MacOSX
```bash
lsof -nP -i4TCP:8080 | grep LISTEN
```

Sau đó dùng lệnh kill
```bash
sudo kill -9 process_id
```

Sanic hỗ trợ jinja2 template
https://github.com/huge-success/sanic/issues/113

https://github.com/lixxu/sanic-jinja2

https://www.fullstackpython.com/sanic.html

https://github.com/huge-success/sanic/wiki/Examples
https://github.com/huge-success/sanic/wiki/Extensions