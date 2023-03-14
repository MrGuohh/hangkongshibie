# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/11 23:28
import tensorflow as tf

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
# 加载神经网络模型
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=50))
model.add(Dense(units=1, activation='sigmoid'))
model.load_weights('D:/实习2/data/my_model_weights.h5')
# 加载数据集
test_data = pd.read_csv('D:/实习2/data/data/test5.csv')
# 对数据集进行预测
predictions = model.predict(test_data)
print(predictions)
result = np.where(predictions > 0.5, 1, 0)
# 输出预测结果
print(result)
df = pd.DataFrame(result, columns=['emd_lable2'])
df2 = pd.DataFrame(predictions, columns=['emd_lable2'])
df.to_csv('result.csv', index=False)
df2.to_csv('result2.csv', index=False)