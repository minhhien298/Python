import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("OfficeSupplies.csv")
df.shape  # In ra kích thước dữ liệu (5000, 14) 5000 dòng, 14 cột
df.head(6)  # Trả dữ liệu mẫu, mặc định là 5 dòng đầu tiên
df.dtypes  # In ra kiểu dữ liệu từng cột
df.describe()

df.isnull().values.any() # Kiểm tra có cell nào bị null không?

# Sắp xếp
sort_by_unit = df.groupby(["Rep"]).sum().sort_values("Units", ascending=False)
print(sort_by_unit)

# Tạo thêm một cột Total Price trong data frame
df["Total Price"] = df["Units"] * df["Unit Price"]
df.head()

# Lần này sort theo Total Price chứ không theo Units nữa
print(df.groupby("Rep").sum().sort_values("Total Price", ascending=False).head())

# Doanh số theo vùng
sales_by_region = df.groupby(["Region"])['Total Price'].sum()
print(sales_by_region) # In ra debug

# Vẽ đồ thị
sales_by_region.plot(kind='bar', legend=True)

plt.show()