import numpy as np
from numpy.matrixlib.defmatrix import matrix

#Tạo ma trận 3x3 với giá trị ngẫu nhiên
# matrix = np.random.rand(3,3)
#
# print("Ma trận gốc ngẫu nhieen: \n",matrix)
# # Truy cập từng phần tử
# print("\nPhần tử hàng 0, cột 0:", matrix[0, 0])
# print("Phần tử hàng 1, cột 2:", matrix[1, 2])
# print("Hàng đầu tiên:", matrix[0])
# print("Cột cuối cùng:", matrix[:, -1])
# print("Hàng cuối cùng: ", matrix[-1])
# print("Hàng cuối cùng và hàng đầu tiên: ", matrix[-1], matrix[0])
# print("Cột đầu tien: ", matrix[:,0])


#Tạo matrix 3x3
matrix = np.random.rand(3,3)
print("Ma trận ", matrix)

#Tính trung bình , phương sai, độ lệch chuẩn
print("\nTrung bình: ", np.mean(matrix))
print("Phuong sai: ", np.var(matrix))
print("Độ lệch chuẩn ", np.std(matrix))

# Giá trị lớn nhất và nhỏ nhất trên từng hàng và cột
print("\nGiá trị lớn nhất trên từng hàng:", np.max(matrix, axis=1))
print("Giá trị nhỏ nhất trên từng cột:", np.min(matrix, axis=0))