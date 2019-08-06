# Format string kiểu cũ, khá khó đọc và dễ bị lỗi

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"

print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." %
      (first_name, last_name, age, profession, affiliation))

name = "Eric"
print("Hello, {}. You are {}.".format(name, age))