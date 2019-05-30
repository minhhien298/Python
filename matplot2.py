import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

data = {1940: 120, 1941: 122, 1942: 130, 1943: 110, 1944:154, 1945: 165, 1946: 134, 1947: 128, 1948: 180, 1949: 170, 1950:180, 1951:192} # Tạo dictionary

year = np.array(list(data.keys()))
films = np.array(list(data.values()))

# Thủ thuật làm mềm bằng đường cong bezier nối qua các điểm
year_smooth = np.linspace(year.min(), year.max(), 100) # bổ xung thêm nhiều điểm trung gian cho mịn
spl = make_interp_spline(year, films, k=2) # Hàm Bezier bậc 2
film_smooth = spl(year_smooth)

plt.plot(year_smooth, film_smooth)
plt.title("Drama Film by year")
plt.show()