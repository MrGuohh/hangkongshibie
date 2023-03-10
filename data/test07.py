# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/9 16:17
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv('D:/实习2/data/data/new_data.csv')
X = data.drop(['emd_lable'], axis=1).values
y = data['emd_lable'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X_train, y_train, epochs=100, batch_size=32)


loss_and_metrics = model.evaluate(X_test, y_test, batch_size=128)

y_pred = model.predict(X_test)