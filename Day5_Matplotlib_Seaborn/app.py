import matplotlib.pyplot as plt

# Dữ liệu giả lập về giá cổ phiếu
ngay = ["Mon", "Tue", "Wed", "Thu", "Fri"]
gia_co_phieu = [100, 105, 102, 110, 120]

# Vẽ biểu đồ đường
plt.plot(ngay, gia_co_phieu, marker="o",linewidth=2,linestyle=":", color="b", label="Giá cổ phiếu")

# Thêm tiêu đề và nhãn
plt.title("Xu hướng giá cổ phiếu")
plt.xlabel("Ngày")
plt.ylabel("Giá")
plt.legend()
plt.show()
# Dữ liệu giả lập về doanh thu
cua_hang = ["Store A", "Store B", "Store C", "StoreD"]
doanh_thu = [5000, 7000, 6000, 90000]

# Vẽ biểu đồ cột
plt.bar(cua_hang, doanh_thu, color=["yellow", "red","blue"])


# Thêm tiêu đề và nhãn
plt.title("Doanh thu của các cửa hàng")
plt.xlabel("Cửa hàng")
plt.ylabel("Doanh thu")
plt.show()
import numpy as np

# Dữ liệu giả lập
dien_tich = np.random.randint(50, 200, 30)  # Diện tích nhà
gia_ban = dien_tich * 500 + np.random.randint(-10000, 10000, 30)  # Giá bán

# Vẽ biểu đồ tán xạ
plt.scatter(dien_tich, gia_ban, color="purple", alpha=0.5)

# Thêm tiêu đề và nhãn
plt.title("Mối quan hệ giữa diện tích nhà và giá bán")
plt.xlabel("Diện tích (m²)")
plt.ylabel("Giá bán (triệu VND)")
plt.show()


import seaborn as sns

# Dữ liệu giả lập về lương
luong = [3000, 3500, 4000, 5000, 6000, 10000, 12000, 25000]  # Có outlier 25000

# Vẽ Boxplot
sns.boxplot(y=luong)
plt.title("Phân phối lương nhân viên")
plt.show()

import pandas as pd

# Dữ liệu giả lập
data = {
    "Diện tích": np.random.randint(50, 200, 50),
    "Giá bán": np.random.randint(100000, 500000, 50),
    "Số phòng ngủ": np.random.randint(1, 5, 50)
}
df = pd.DataFrame(data)

# Vẽ Heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Tương quan giữa các biến")
plt.show()
