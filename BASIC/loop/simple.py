"""

for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break


for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)


for i in [0, 1, 2, 3, 4]:
    print(i)

"""
for i in ["0", 1, "2", 3, "4"]:
    print(i)