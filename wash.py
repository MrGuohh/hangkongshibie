import pandas as pd
#import tensorflow as tf
import numpy as np
"""df = pd.read_csv('selected_features.csv')
df.fillna(value=0, inplace=True)
df.drop_duplicates(inplace=True)"""



# 读取 CSV 文件并转换为 DataFrame
data = pd.read_csv('selected_features.csv')

# 选择需要清洗的列
columns_to_clean = ['pax_fcny']

# 计算每列的均值和标准差
means = data[columns_to_clean].mean()
stds = data[columns_to_clean].std()

# 根据均值和标准差计算异常值范围
lower_bounds = means - 3 * stds
upper_bounds = means + 3 * stds
print(lower_bounds)
print(upper_bounds)
# 将异常值替换为均值
for col in columns_to_clean:
    data.loc[data[col] < lower_bounds[col], col] = means[col]
    data.loc[data[col] > upper_bounds[col], col] = means[col]
# 保存清洗后的数据到新的 CSV 文件
# data.to_csv('clean_data.csv', index=False)
