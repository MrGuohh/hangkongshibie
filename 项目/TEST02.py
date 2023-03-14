


"""# 分割数据集为特征和目标变量
X = data.drop('emd_lable', axis=1)#将数据集 data 中的名为 emd_lable的列从数据集中删除，
y = data['emd_lable']
# 标签编码
encoder = LabelEncoder()
X_encoded = X.apply(encoder.fit_transform)
# 使用 SelectKBest 进行单变量特征选择
selector = SelectKBest(score_func=f_regression, k=10)  # 选择最佳的 5 个特征
X_new = selector.fit_transform(X_encoded, y)
# 输出选择的特征
selected_features = X.columns[selector.get_support()]
print(selected_features)
#data.to_csv('hh.csv', index=False)"""
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

# 读取 CSV 文件
data = pd.read_csv("TEST01.csv")

# 分离目标变量
X = data.drop(['emd_lable'], axis=1)
y = data['emd_lable']

# 按照数据类型选择数值型特征
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# 使用 SelectKBest 进行单变量特征选择
k_best = SelectKBest(score_func=f_classif, k=10)
X_best = k_best.fit_transform(X[numeric_features], y)

# 打印选择的特征
selected_features = X[numeric_features].columns[k_best.get_support()].tolist()
print("Selected Features:", selected_features)