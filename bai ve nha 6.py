import math
print("nhap phuong trinh ax2 + bx + c = 0")
while True:
    try:
        A = float(input("nhap a ="))
        B = float(input("nhap b ="))
        C = float(input("nhap c ="))
        break;
    except Exception:
        print(" a, b, c must be number, try again")
if A == 0:
    x = -C/B
    print("nghiem x:",x)
if A != 0:
    delta = B*B - 4*A*C
    if delta < 0:
        print("no solution")
    elif delta == 0:
        x12 = -B/2/A
        print("x1 = x2 =",x12)
    else:
        x1 = (-B + math.sqrt(delta))/2/A
        x2 = (-B + math.sqrt(delta))/2/A
        print("x1=",x1)
        print("x2=",x2)