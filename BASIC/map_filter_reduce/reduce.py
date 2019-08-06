product = 1
nums = [1, 2, 3, 4]
for num in nums:
    product = product * num
print(product)

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

# Tính tổng
total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)
