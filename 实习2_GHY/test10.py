# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/10 22:17
import pandas as pd
from sklearn.preprocessing import LabelEncoder
test_data = pd.read_csv('D:/实习2/data/first.csv',low_memory=False)

label_encoders = {}
for col in test_data.columns:
    if test_data[col].dtype == 'object':
        label_encoders[col] = LabelEncoder()
        test_data[col] = label_encoders[col].fit_transform(test_data[col].astype(str))
test_data.to_csv("second.csv", index=False)