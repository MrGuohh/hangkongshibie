# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/11 0:31
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 读取CSV文件
data = pd.read_csv('D:/实习2/test1.csv')

# 分离输入数据和标签
X = data.drop('emd_lable2', axis=1)
y = data['emd_lable2']

# 使用StandardScaler对数据进行标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 将标准化后的数据保存到新的CSV文件
X_df = pd.DataFrame(X, columns=data.columns[:-1])
normalized_data = pd.concat([X_df, y], axis=1)
normalized_data.to_csv('test2.csv', index=False)