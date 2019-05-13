# tim giai thua

def giaithua(so):
    if so == 1:
        return 1
    else:
        return (so*giaithua(so-1))

print("Mời bạn nhập cái gì đó:")
s= input()
print(giaithua(int(s)))