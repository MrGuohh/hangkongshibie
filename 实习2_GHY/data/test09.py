# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/10 16:54

# 加载测试数据集
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from keras.models import load_model

# 准备测试数据
test_data = pd.read_csv('D:/实习2/test4.csv')
#df1=pd.read_csv('D:/实习2/data/data/test.csv')
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# 加载模型
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=50))
model.add(Dense(units=1, activation='sigmoid'))
model.load_weights('D:/实习2/data/my_model_weights.h5')

# 使用模型进行预测
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)

# 评估模型
print(y_pred)
accuracy = np.mean(y_pred == y_test)
print('Accuracy: %.2f%%' % (accuracy * 100))