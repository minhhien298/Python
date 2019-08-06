d = {}  # empty dict
d = {'first_name': 'Trịnh', 'last_name': 'Cường', 'age': 20}

d['first_name'] = "Nguyễn"
print(d)

# Cách khác để chạy
e = dict(first_name="Trịnh", last_name="Cường", age=30)
print(e)

for key in e:
    print(key, d[key])
