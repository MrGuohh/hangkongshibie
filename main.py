import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder
# 加载数据集
data = pd.read_csv("train.csv")
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data = pd.read_csv("train.csv", dtype={"column51": str, "column52": str})
data = data.astype(str)
data.fillna(0, inplace=True)#将数据集 data 中的缺失值（NaN）用 0 来填充，inplace=True 表示对原数据集进行修改，而不是创建一个新的数据集
data.drop_duplicates(inplace=True)#删除数据集 data 中的重复行
data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=50)  # 选择最佳的 50 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print('Selected features:', selected_features)