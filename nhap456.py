import csv
import matplotlib.pyplot as plt

x = []
y = []

with open('sample/data.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv

    for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
        x.append(row[0])
        y.append(row[1])

plt.scatter(x, y, s=50, c='orange')
plt.show