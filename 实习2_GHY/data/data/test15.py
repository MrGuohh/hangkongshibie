# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/12 23:03
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv('D:/实习2/train.csv',low_memory=False)
'''label_encoders = {}
for col in data.columns:
    if data[col].dtype == 'object':
        label_encoders[col] = LabelEncoder()
        data[col] = label_encoders[col].fit_transform(data[col].astype(str))'''
#data.to_csv('train.csv', index=False)#
# 分割数据集为特征和目标变量
X = data.drop('emd_lable2', axis=1)#将数据集 data 中的名为 emd_lable2的列从数据集中删除，
y = data['emd_lable2']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)

# 选择最相关的特征因子
selector = SelectKBest(chi2, k=10)
X_new = selector.fit_transform(X_encoded, y)

# 输出选择的特征因子
selected_features = X.columns[selector.get_support()]
print(selected_features)
