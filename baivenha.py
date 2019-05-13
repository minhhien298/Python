


# bai 2 Tong 2 so bang so input
print("Mời bạn nhập cái gì đó:")
s= input()
s= int(s)
for a in range(1,100):
    for b in range(1, 100):
        if a + b == int(s):
            print(str(a),str(b))
        elif a==b:
            break