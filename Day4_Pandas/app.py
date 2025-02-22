# Mục tiêu:
#
# Hiểu Pandas và cách nó giúp xử lý dữ liệu AI hiệu quả.
# Biết cách đọc, xử lý, làm sạch và trực quan hóa dữ liệu với Pandas.
# Ứng dụng Pandas vào chuẩn bị dữ liệu trước khi huấn luyện mô hình AI.

'''
 Khái niệm cần học trong Pandas
🔹 Series & DataFrame – Hai cấu trúc dữ liệu quan trọng trong Pandas.
🔹 Đọc và ghi dữ liệu – Làm việc với CSV, Excel, SQL, JSON.
🔹 Truy cập và xử lý dữ liệu – Lọc dữ liệu, xử lý missing values.
🔹 Thống kê dữ liệu – Tính trung bình, phương sai, độ lệch chuẩn.
🔹 Chuẩn bị dữ liệu cho mô hình AI – Xử lý outlier, feature scaling, encoding.
'''
from uu import encode

import pandas as pd
import numpy as np
# import pandas as pd
#
# data = [10, 20, 30, 40]
# series = pd.Series(data, name="Giá trị")
# print(series)

#this is a dictionary, key = column labels, value = column value with DataFrame => n-dimensional
# data = {
#     "Tên": ["Alice", "Bob", "Charlie"],
#     "Tuổi": [25,30,35],
#     "Lương": [5000, 6000, 7600]
# }
# df = pd.DataFrame(data)
# print(df)
# Tạo DataFrame mẫu
data = {
    "Ten": ["Alice", "Bob", "Charlie", "David"],
    "Luong": [5000, 7000, np.nan, 8000]
}
df = pd.DataFrame(data)

# Lọc dữ liệu: chỉ lấy người có lương > 6000
filtered_df = df[df["Luong"] > 6000]
print("Người có lương > 6000:\n", filtered_df)

# Xử lý missing values: điền bằng giá trị trung bình
df["Luong"] = df["Luong"].fillna(df["Luong"].mean())
print("\nDataFrame sau khi xử lý missing values:\n", df)


#Bài tập 5: Chuẩn b dữ liệu cho mô hình AI
# Chuẩn hóa dữ liệu lương về khoảng [0,1] bằng Min-Max Scailing
#Chuyeen cot ten thành số Label Encoding
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Chuẩn hóa cot luong
scaler = MinMaxScaler()
df["Luong_scaled"] = scaler.fit_transform(df[["Luong"]])
# df["Lương"] → Trả về Series (mảng 1D) ⛔ MinMaxScaler yêu cầu mảng 2D
# df[["Lương"]] → Trả về DataFrame (mảng 2D) ✅ Đúng định dạng

#Encoding cột Tên
encoder = LabelEncoder()
df["Ten_encoded"] = encoder.fit_transform(df["Ten"])
print("\nDataFrame sau khi chuẩn bị dữ liệu\n", df)

#Self là tham số bắt buôộc khi định nghĩa method trong các Class/Object