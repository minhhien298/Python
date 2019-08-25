# Hướng dẫn sử dụng session
https://sanic-session.readthedocs.io/en/latest/using_the_interfaces.html

## Sử dụng in memory để lưu session
```bash
python3 main.py
```

## Sử dụng redis để lưu session
Cần tạo redis container
```bash
docker-compse up -d
python3 session_redis.py

```