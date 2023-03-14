import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
#import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('train.csv',low_memory=False,encoding='utf-8')
print(data)
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=50)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print(selected_features)

#data.to_csv('clean_data.csv', index=False)