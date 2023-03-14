import numpy as np
import pandas as pd

data = pd.read_csv('train-checkpoint.csv')  # 读取文件

import pandas as pd

# 读取原始数据文件
#data = pd.read_csv('raw_data.csv')

# 处理缺失值
data = data.dropna()

# 处理重复数据
data = data.drop_duplicates()

# 处理异常值
#data = data[(data['value'] > 0) & (data['value'] < 100)]

# 导出清洗后的数据文件
#data.to_csv('clean_data.csv', index=False)

print(data)