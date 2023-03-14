"""import pandas as pd
import torch
import tensorflow as tf
data = pd.read_csv('test_prepare.csv')
jfk_data = data['prebuy_i_cnt_y3_d99'].values

jfk_tensor = torch.tensor(jfk_data)

jfk_tensor = tf.convert_to_tensor(jfk_data)
# 保存修改后的数据到 CSV 文件
data.to_csv('file.csv', index=False)"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
test_data = pd.read_csv('test_train.csv',low_memory=False)

label_encoders = {}
for col in test_data.columns:
    if test_data[col].dtype == 'object':
        label_encoders[col] = LabelEncoder()
        test_data[col] = label_encoders[col].fit_transform(test_data[col].astype(str))
test_data.to_csv("test_train2.csv", index=False)