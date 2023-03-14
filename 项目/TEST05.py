import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import torch
from sklearn.preprocessing import StandardScaler
from keras.models import load_model

# 准备测试数据
test_data = pd.read_csv('selected_features2.csv')

"""jfk_data = test_data['prebuy_i_cnt_y3_d99'].values

jfk_tensor = torch.tensor(jfk_data)

jfk_tensor = tf.convert_to_tensor(jfk_data)"""
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# 加载模型
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=9))
model.add(Dense(units=1, activation='sigmoid'))
model.load_weights('my_model_weights.h5')

# 使用模型进行预测
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)

# 评估模型
accuracy = np.mean(y_pred == y_test)
print('Accuracy: %.2f%%' % (accuracy * 100))