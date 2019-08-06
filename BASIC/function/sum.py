def sum(*args):
    temp = 0
    for num in args:
        temp += num
    return temp


print(sum(1, 2, 3, 4, 5, 6))

print(sum(1, "2", "3"))  # Đoạn này sẽ gây lỗi
