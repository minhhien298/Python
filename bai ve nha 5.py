import random

somay = random.randrange(1, 6)
for i in range(1, 7):
    print("Nhap so di ")
    sonhap = int(input())
    if sonhap == somay:
        print("Dung roi")
        break
    elif sonhap < somay:
        print("be qua")
    elif sonhap > somay:
        print("lon qua ")
