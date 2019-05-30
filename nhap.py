import matplotlib.pyplot as plt

data = {1940: 120, 1941: 122, 1942: 130, 1943: 110, 1944:154, 1945: 165, 1946: 134,
        1947: 128, 1948: 180, 1949: 170, 1950:180, 1951:192} # Tạo dictionary
year = list(data.keys())
films = list(data.values())

plt.plot(year, films)
plt.title("Drama Film by year")

plt.legend()
plt.show()