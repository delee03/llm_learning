import numpy as np

matrix = np.random.randint(1, 101, size=(3, 3))

print("Dữ liệu gốc:\n", matrix)

#Matrix max scailing để chuẩn hóa dữ liệu về khoảng [0,1]
min_val = np.min(matrix)
max_val = np.max(matrix)
normalized_data = (matrix - min_val)/(max_val - min_val)
print("Min-Max scailling: \n", normalized_data)

### Các khác chuẩn hóa data c độ lech lớn hơn
# Z-score Normalization
mean = np.mean(matrix)
std = np.std(matrix)
z_score_data = (matrix - mean) / std
print("Dữ liệu sau Z-score Normalization:", z_score_data)
## Mục tiêu: Numpy giúp hiểu rõ hơn về dữ liệu và tính toán dữ liệu nhanh chóng dễ dàng , giúp xác định bước pre-processing data more efficient
