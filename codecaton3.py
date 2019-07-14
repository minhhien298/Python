# 1. Vẽ đồ thị data.csv

import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import datasets, linear_model


with open('sample/data.csv') as csv_file:  # mở file csv
    csv_reader = csv.reader(csv_file)  # đọc file csv
    x = []
    y = []

    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

a = np.array(x).reshape((-1, 1))
b = np.array(y)
model = LinearRegression()
model.fit(a, b)
model = LinearRegression().fit(a, b)
r_sq = model.score(a, b)
print('coefficient of determination:', r_sq)
plt.plot(a,b)

# Fixing random state for reproducibility
# np.random.seed(19680801)
print(x)
print(y)
print(a)
print(b)

N = 50
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x,y, s=2, c='red')
plt.show()


#Chuyển sang ảnh đen trắng
#Sử dụng Gassian Blur để làm mờ ảnh
#Gợi ý: Google tìm cách làm. Keyword: OpenCV
import cv2 #package để xử lý ảnh

#đọc file ảnh con mèo
img = cv2.imread('sample/cat.jpg')
#chuyển ảnh con mèo về dạng grey color
greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply threshold để chuyển thành ảnh đen trắng
(thresh, BlackAndWhiteImg) = cv2.threshold(greyimg, 127, 255, cv2.THRESH_BINARY)

# gaussian blur
#dùng hàm GaussianBLur để làm mờ
blurimg = cv2.GaussianBlur(img, (5, 5), 0)
blurBlackAndWhite = cv2.GaussianBlur(BlackAndWhiteImg, (5, 5), 0)

#show result

cv2.imshow('original cat', img)
cv2.imshow('blurred cat', blurimg)

cv2.imshow('black and white cat', BlackAndWhiteImg)
cv2.imshow('blurred black and white cat', blurBlackAndWhite)

cv2.waitKey(0)
cv2.destroyAllWindows()




