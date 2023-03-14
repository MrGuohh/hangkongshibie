import sklearn
import numpy as np
import csv
import pandas as pd
from pandas import Series, DataFrame
input_csv_file = 'test.csv'
df1 = pd.read_csv(input_csv_file)
input_load_mat = df1.values
np.set_printoptions(precision=2, suppress=True)
df1 = df1.dropna()
##print(input_load_mat)
##print(df1.info())
print(df1.head())
print(df1.isnull())
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
input_csv_file = 'test.csv'
df1 = pd.read_csv(input_csv_file)
# 读取原始数据文件

# 处理缺失值
df1 = df1.dropna()

# 处理重复数据
df1 = df1.drop_duplicates()
print(df1)
# 处理异常值
df1 = df1[(df1['value'] > 0) & (df1['value'] < 100)]

# 导出清洗后的数据文件
df1.to_csv('clean_data.csv', index=False)

# 加载数据集
#data = load_digits().data

# 实例化 PCA 对象，将数据降到 2 维
pca = PCA(n_components=50)

# 将数据投影到主成分上
new_data = pca.fit_transform(df1)

# 输出新的数据形状
print(new_data.shape)
