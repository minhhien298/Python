# **kwargs cho phép hàm nhận nhiều tham số nhưng phải có tên tham số
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(a="Hello", b="World", c="John")

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
greet_me(**kwargs)