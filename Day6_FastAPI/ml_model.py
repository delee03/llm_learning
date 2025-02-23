from sklearn.linear_model import LinearRegression

import numpy as np

#Dữ liệu giả lap (Dien tich -> gia nha)
x = np.array([[50], [60], [70], [80], [90]]) #to create a 2D array (a column vector) which is required by the LinearRegression model from sklearn.
y = np.array([100000, 120000, 140000, 160000, 180000])

#Train model
model = LinearRegression()
model.fit(x, y)

#Formula of Linear Regression (supervised learning) :
# y = w0 + w0x0 + w1x1 + ... + wnxn => model unsderstand the w = weighs and the result is y=20x
# {
#     x = features
# }
print("Hệ số hồi quy (w1):", model.coef_[0])
print("Giá trị chặn (w0):", model.intercept_)
# Hệ số hồi quy (w1): 1999.9999999999998 =>  Khi diện tích nhà tăng 1m², giá nhà tăng 2000 VND.
# Giá trị chặn (w0): 2.9103830456733704e-11 =>  Khi diện tích là 0m², giá nhà là 1 con số tiny (mô hình đơn giản).
#KẾt luật: sau khi train model đã tìm ra quy luật y = 20x
def predict_price(area: float):
    return  model.predict([[area]])[0]
