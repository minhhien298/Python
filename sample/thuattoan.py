def fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        a_i_2 = 0
        a_i_1 = 1
        for i in range(2, n + 1):
            a = a_i_2 + a_i_1
            a_i_2 = a_i_1
            a_i_1 = a
        return a



list = []
#n = int(input("dien so tu nhien vao day: "))
list.append(0)
#if n < 1:
 #   print(list)
#if n == 1:
  #  list.append(1)
   # print(list)
#if n > 1:
 #   temp = 0
  #  list.append(1)
   # while temp < n:
    #    temp = int(list[-1]) + int(list[-2])
     #   list.append(temp)


def ptb2():
    #a = int(input("dien so tu nhien vao day: "))
    #b = int(input("dien so tu nhien vao day: "))
    #c = int(input("dien so tu nhien vao day: "))

    #elta = b** -4*a*c

    if delta < 0:
        print("vo nghien")
#    else delta == 0:
        print(int())

def pi(N: int) -> float:
    heso = 1
    sum = 0
    for i in range(1, N):
        print(2 * i - 1)
        sum += heso/(2*i-1)
        heso = - heso
    return sum * 4.0

from time import time

def reverse_slicing(s: str) -> str:
   return s[::-1]

start = time()
for _ in range(10000):
    reverse_slicing("HLW")
delta = (time()-start) *100000
# print(f"{delta:6.0f} micro-seconds")


class Car:
   def __init__(self, manufacturer, model):
       self.manufacturer = manufacturer
       self.model = model

   def __str__(self):
       return f"{self.model} by {self.manufacturer}"

   def run(self):
       print("car runs")

   def stop(self):
       print("car stops")
fadil = Car("Vinfast", "Fadil")
fadil.run()
fadil.stop()
print(fadil)

triton = Car("Mitsubishi", "Triton")
triton.run()
print(triton)
