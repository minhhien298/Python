#1. Cho một mảng gồm N số tự nhiên
#Hãy viết một hàm tham số đầu vào là một mảng các số tự nhiên trả về một mảng gồm các ký tự + hoặc - hay = mô tả phần tử tiếp theo tăng hay giảm hay bằng so với phần tử trước đó
#sign = "+" if A[i+1] > A[i] else "-" if A[i+1] < A[i] else "=" Ví dụ: m = [1, 4, 4, 2, 3, 6, 7, 8, 5, 5] def inc_or_dec(array):->[String]
#Kết quả trả về sẽ là ['+', '=', '-', '+', '+', '+', '+', '-', '=']
def congtru(A):
    mangtam = []
    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            mangtam.append("+")
        elif A[i] == A[i-1]:
            mangtam.append("=")
        elif A[i] < A[i-1]:
            mangtam.append("-")
    print(mangtam)

#2. Tính số PI
def pi(N):
    heso =1
    sum = 0
    for i in range(1,N):
        sum += heso/(2*i-1)
        heso =-heso
    print(sum*4)

#Cho file sales100.csv hãy đọc file này và trả về các kết quả sau đây:

import csv

with open('sample/sales100.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    revenueBF = 0
    genre_setregion = set()
    genre_setitem = set()
    genre_dic = dict()
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            # Liệt kê tất cả các region, sắp xếp A-Z và chỉ hiển thị mỗi region một lần.
            genres = row[1].split('|')
            #revenu = int(row[12].split('|'))

            # Tương tự liệt kê tất cả các item type, sắp xếp A-Z và chỉ hiển thị mỗi region một lần.
            genre_setregion |= set(genres)
            genres2 = row[2].split('|')

            # Tính tổng doanh thu Total Revenue của item type "Baby Food" trên tất cả các dòng
            if genres2 == ['Baby Food']:
                revenueBF += float(''.join(row[11].split('|')))
            genre_setitem |= set(genres2)

            # Đối với từng item type, sau khi sắp xếp A-Z hãy tính tổng doanh thu TotaRevenue


            line_count += 1
    listphim = list(sorted(genre_setregion))
    listitem = list(sorted(genre_setitem))

    print(listphim)
    print(listitem)
    print(revenueBF)
    print(genre_dic)




# Đối với từng item type, sau khi sắp xếp A-Z hãy tính tổng doanh thu TotaRevenue

import csv
from collections import defaultdict
result = defaultdict(int)

with open('sample/sales100.csv', encoding="utf8") as in_file:
    csv_reader = csv.reader(in_file)  # đọc file csv
    next(csv_reader, None)

    for row in csv_reader:
        key = row[2]
        if key in result:
            pass
        result[key] += float(row[11])
print(sorted(result.items(), key=lambda kv: kv[0]))



import csv

with open('sales100.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv

    count = 0
    revenue_per_item_type = {}  # Empty dictionary
    for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
        if count > 0:
            if revenue_per_item_type.get(row[2]) is None:
                revenue_per_item_type[row[2]] = float(row[11])
            else:
                revenue_per_item_type[row[2]] += float(row[11])

        count += 1

# In ra kết quả chưa sắp xếp key của dictionary
print(revenue_per_item_type)

# Sắp xếp lại dictionary
for item_type in sorted(revenue_per_item_type.keys()):
    print(item_type, revenue_per_item_type[item_type])

# https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file
# https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file




if __name__== "__main__":

    congtru([1, 4, 4, 2, 3, 6, 7, 8, 5, 5])
    pi(1000000)

