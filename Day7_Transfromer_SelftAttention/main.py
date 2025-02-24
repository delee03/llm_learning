import numpy as np

# Tạo Q, K, V giả lập (3 từ trong câu, vector 4 chiều)
Q = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1]])
K = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1]])
V = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 1.0, 1.1, 1.2]])

# Bước 1: Tính QK^T
score = np.dot(Q, K.T)

# Bước 2: Chia cho sqrt(d_k)
dk = Q.shape[1]  # Số chiều của vector Q
scaled_score = score / np.sqrt(dk)

# Bước 3: Áp dụng Softmax
attention_weights = np.exp(scaled_score) / np.sum(np.exp(scaled_score), axis=1, keepdims=True)
#This is sofmax = probability distribution always = 1


# Bước 4: Nhân với V
output = np.dot(attention_weights, V)

print("Attention Weights:\n", attention_weights)
print("\nOutput:\n", output)
