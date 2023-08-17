from sklearn.datasets import load_iris
import pandas as pd
import mglearn
import numpy as np

iris_dataset = load_iris()


from sklearn.model_selection import train_test_split

# 학습데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset["data"], iris_dataset["target"], random_state=0
)

iris_datatrame = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# 화면에 그림을 그림
pd.plotting.scatter_matrix(
    iris_datatrame,
    c=y_train,
    figsize=(15, 15),
    marker="o",
    hist_kwds={"bins": 20},
    s=60,
    alpha=0.8,
    cmap=mglearn.cm3,
)


# 모델 학습
from sklearn.neighbors import KNeighborsClassifier  # KNN 모델 (얼마만큼 서로 인접한지 분류)

model = KNeighborsClassifier(n_neighbors=1)  # n_neighbors=1 : 이웃이 하나라는 뜻
model.fit(X_train, y_train)

X_new = np.array([[4.3, 2.9, 0.7, 0.2]])
prediction = model.predict(X_new)
print(f"예측: {prediction}")
print(f"예측한 타깃의 이름: {iris_dataset['target_names'][prediction]}")


# 모델 테스트
y_p = model.predict(X_test)
print(f"테스트 세트에 대한 예측값: {y_p}")
print(f"테스트 세트에 대한 실제값: {y_test}")
print("테스트 세트의 정확도: {:.2f}".format(np.mean(y_p == y_test)))
print("테스트 세트의 정확도: {:.2f}".format(model.score(X_test, y_test)))
