name = "Eric"
age = 74

# Dùng f string trực quan, ít lỗi hơn
print(f"Hello, {name}. You are {age}.")

# Evaluate hàm tính toán
print(f"{2 * 37}")


def to_lowercase(text):
    # Định nghĩa hàm lower case mới
    return text.lower()


name = "Eric Idle"
# gọi hàm bên trong f string
print(f"{to_lowercase(name)} is funny.")

print(f"{name.lower()} is funny")