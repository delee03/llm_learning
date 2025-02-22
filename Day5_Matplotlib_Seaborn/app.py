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
