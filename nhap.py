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

# print(fibo(10))


def cong_simpler(*args):
 return sum(args)

def reverse_for_loop(s: str) -> str:
  s1 = ''
  for c in s:
   s1 = c + s1  # appending chars in reverse order
  return s1


def chap2mang(array1,array2):
    array3 = array1 + array2
    array3.sort(key = int, reverse = False)
    # print(array3)

#Cho một mảng gồm N số tự nhiên m = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4]
#1.1. Hãy tính tổng các phần tử thuộc m
#1.2. Tìm số lớn nhất trong m
#1.3. Tính trung bình cộng các phần tử trong m
#1.4. In mảng trên theo thứ tự nghịch đảo 4, 2, 12, 9, 5, 8, 7, 6, 3, 2, 4, 1
#1.5. (Khó) Hãy tìm cách loại những phần tử xuất hiện lặp lại. m' = [1, 4, 2, 3, 6, 7, 8, 5, 9, 12]
#1.6. In ra khoảng cách giữa các phần tử: D[i] = m[i+1] - m[i] D = [3, -2, 1, 3, 1, 1, -3, 4, 3, -10, 2]

def tongcuamang(array):
    print(sum(array))

def timlonnhat(array):
    print(max(array))

def timtrungbinh(array):
    print(sum(array)/len(array))

def nghichdao(array):
    array.reverse()
    print(array)

def botrubglao(array):
    mangtam =[]
    for i in array:
        if i not in mangtam:
            mangtam.append(i)
    print(mangtam)

def khoangcach(array):
    mangtam = []
    for i in range(1,int(len(array))):
        mangtam.append(array[i] - array[i-1])
    print(mangtam)

# Hãy viết một chương trình. Chương trình này sẽ sinh ngẫu nhiên một số nguyên dương trong khoảng từ 0 đến 100 nhưng sẽ giấu kín. Chương trình mời người dùng nhập vào một số dự đoán, chương trình sẽ trả lời số lớn hơn hay nhỏ hơn số ngẫu nhiên được giấu kín. Nếu bằng chương trình báo người chơi đoán đúng và dừng.

import random

def dudoan():
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


def dieukien(array):
    mangtam4 =[]
    for i in range(1,int(len(array))):
        if (array[i] < array[i-1]):
            mangtam4.append(i)
    print(mangtam4)
    mangtam5 = []
    for i in range(1,int(len(mangtam4))):
        mangtam5.append(mangtam4[i] - mangtam4[i-1])
        if (mangtam4[i] - mangtam4[i-1]) == max(mangtam5):
           start = mangtam4[i-1]
    stop = max(mangtam5) + start

    # print(indexcut)
    # print(start)
    print(array[start:stop])


if __name__ == "__main__":

 # print(chap2mang([4,7,9],[1,6,8]))
  tongcuamang([1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4])
  timlonnhat([1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4])
  timtrungbinh([1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4])
  nghichdao([1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4])
  botrubglao([1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4])
  print(list(dict.fromkeys([1, 4, 2, 3, 6, 7, 8, 5, 9, 12, 2, 4])))
  khoangcach([3, -2, 1, 3, 1, 1, -3, 4, 3, -10, 2])
  dudoan()
  dieukien([3, 2, 1, 2, 3, 4, 6, 8, 7, 4, 5, 10, 11, 12, 15, 16, 17, 18, 22, 18, 17])
