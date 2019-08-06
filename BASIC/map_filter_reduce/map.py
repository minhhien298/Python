# Không cần dùng map
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

print(squared)

# Sử dụng map và lambda function
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))


# Lambda function chuyển vào có nhiều hàm
def multiply(x):
    return x*x


def add(x):
    return x+x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)