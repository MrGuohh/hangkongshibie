# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/8 16:39


import pandas as pd
data = pd.read_csv('D:/实习2/train.csv')

selected_data = data[['pax_fcny', 'dist_cnt_y3', 'avg_dist_cnt_y2', 'avg_dist_cnt_y3',
       'dist_all_cnt_y3', 'tkt_3y_amt', 'tkt_i_amt_y3', 'tkt_all_amt_y3',
       'tkt_avg_amt_y2', 'tkt_avg_amt_y3','emd_lable2']]


data = selected_data.drop_duplicates()
data.to_csv('forth.csv', index=False)
