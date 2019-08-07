number_list = range(-5, 5)
print(number_list)

# Chuyển sang array
from array import array
arrayA = array("i", number_list)
print(arrayA)

less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)