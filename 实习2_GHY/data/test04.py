# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/9 10:39
import pandas as pd

# 读取要加入数据的CSV文件
df1 = pd.read_csv('D:/实习2/data/data/train.csv',encoding='gbk')

# 读取要被加入数据的CSV文件
df2 = pd.read_csv('D:/实习2/data/data/new_data.csv')

# 获取要加入的数据列
data_to_add = df1.loc[:, 'emd_lable2']
# 将要加入的数据列加入到要被加入数据的CSV文件中
df_new = pd.concat([df2, data_to_add], axis=1)

# 将新的数据集保存为CSV文件
df_new.to_csv('new_data2.csv', index=False)