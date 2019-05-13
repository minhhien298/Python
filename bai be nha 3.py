# kiem tra so nguyen to

def kt(so):
 so = int(so)
 if so == 1:
  return False
 elif so == 2:
  return True
 elif so ==3:
  return True
 else:
  for i in range(2,so-1):
   if so % i ==0:
    return False
    break
   else:
    return True



print("Mời bạn nhập cái gì đó:")
s= input()
if kt(s) == True:
 print("so nguyuen to")
else:
 print("khong phai so nguyen to ")

