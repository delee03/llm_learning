import numpy as np

def positional_encoding(max_len, d_model):
    pos = np.arange(max_len)[:, np.newaxis]
    i = np.arange(d_model)[np.newaxis, :]
    angle_rates = 1 / np.power(10000, (2 * (i // 2)) / np.float32(d_model))
    pos_encoding = pos * angle_rates

    pos_encoding[:, 0::2] = np.sin(pos_encoding[:, 0::2])  # Áp dụng sin
    pos_encoding[:, 1::2] = np.cos(pos_encoding[:, 1::2])  # Áp dụng cos

    return pos_encoding

# Tính Positional Encoding cho 10 từ, embedding size = 16
pe = positional_encoding(10, 16)
print(pe)
