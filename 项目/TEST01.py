import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
# 读取原始数据文件
data = pd.read_csv('train-checkpoint.csv')

# 处理缺失值

#data.fillna(value=0, inplace=True)
data = data.dropna()

# 处理重复数据
data = data.drop_duplicates()
# 处理异常值
data = data[(data['pax_fcny'] > 0) & (data['pax_fcny'] < 200000)]
columns_to_clean = ['pax_fcny']

means = data[columns_to_clean].mean()
print(means)
stds = data[columns_to_clean].std()
print(stds)

# 根据均值和标准差计算异常值范围
lower_bounds = means - 3 * stds
upper_bounds = means + 3 * stds
print(lower_bounds)
print(upper_bounds)

# 将异常值替换为均值
for col in columns_to_clean:
    data.loc[data[col] < lower_bounds[col], col] = means[col]
    data.loc[data[col] > upper_bounds[col], col] = means[col]
data.to_csv('TEST01.csv', index=False)
