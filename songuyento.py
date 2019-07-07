def songuyeto():
for num in range(1,101):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break
  
  
def  phuongtrinhbac2():
 	a, b, c = 0
	d = b**2-4*a*c
	if (d<0 or a = 0): 
   print("VO NGHIEM")
	elif (d==0): 
   print("X = ", -b/(2*a))
	else:
		print("X1 = ", (-b-d**(0.5))/(2*a))
		print("X1 = ", (-b+d**(0.5))/(2*a))       
            
