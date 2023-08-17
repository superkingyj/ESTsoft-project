import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[30], [40], [50], [60], [70]])
Y = np.array([100, 150, 200, 250, 300])

model = LinearRegression()

# 모델에 학습
model.fit(X, Y)

size = int(input("주택 평수 입력: "))
house_size = np.array([[size]])
predicted_price = model.predict(house_size)

print(f"{size}평수의 월세는? ", predicted_price)
