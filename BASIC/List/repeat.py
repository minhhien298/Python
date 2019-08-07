import itertools

# Cách này phổ biến tạo ra list 10 phần tử giá trị ban đầu là 1
list_int = [1] * 10
print(list_int)

# Tạo ra đối tượng, đối tượng sẽ sinh list 10 phần tử giá trị ban đầu là 0
list_int2 = itertools.repeat(0, 10)
print(list(list_int2))
