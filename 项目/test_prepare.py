import pandas as pd
import numpy as np
import tensorflow as tf
data = pd.read_csv('test.csv')

# 将第二列数据类型转换为浮点数类型
#data['ffp_nbr'] = pd.to_numeric(data['ffp_nbr'], errors='coerce')
"""clean=data['ffp_nbr']
tensor = tf.constant(clean, dtype=tf.float32)"""
# 写回到 CSV 文件
#data.to_csv('test.csv', index=False)
selected_data = data[['emd_lable2', 'ffp_nbr', 'seat_middle_cnt_y3',
                      'prebuy_i_cnt_y2_d99', 'prebuy_i_cnt_y3_d3', 'prebuy_i_cnt_y3_d7',
                      'prebuy_i_cnt_y3_d99', 'avg_dist_cnt_y2', 'pit_avg_amt_y2', 'pit_avg_amt_y3']]
data = selected_data.dropna()
data['ffp_nbr'] = np.zeros_like(data['ffp_nbr'])
data = selected_data.drop_duplicates()
print(data)
data.to_csv('test_prepare.csv', index=False)