# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/9 9:05
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
# 读取原始数据文件
data = pd.read_csv('D:/实习2/second.csv')

# 处理缺失值

#data.fillna(value=0, inplace=True)
data = data.dropna()

# 处理重复数据
data = data.drop_duplicates()
# 处理异常值
data = data[(data['pax_fcny'] > 0) & (data['pax_fcny'] < 200000)]
columns_to_clean = ['pax_fcny']

means = data[columns_to_clean].mean()
print(means)
stds = data[columns_to_clean].std()
print(stds)

# 根据均值和标准差计算异常值范围
lower_bounds = means - 3 * stds
upper_bounds = means + 3 * stds
print(lower_bounds)
print(upper_bounds)

# 将异常值替换为均值
for col in columns_to_clean:
    data.loc[data[col] < lower_bounds[col], col] = means[col]
    data.loc[data[col] > upper_bounds[col], col] = means[col]
data.to_csv('third.csv', index=False)

'''columns_to_normalize = ['seg_route_to', 'seg_flight', 'seg_cabin', 'pax_fcny', 'emd_lable',
       'gender', 'age', 'residence_country', 'cabin_c_cnt_y2',
       'cabin_c_cnt_y3', 'pref_aircraft_y1_4', 'pref_aircraft_y1_5',
       'pref_aircraft_y2_1', 'pref_aircraft_y2_2', 'pref_aircraft_y2_3',
       'pref_aircraft_y2_4', 'pref_aircraft_y2_5', 'pref_aircraft_y3_1',
       'pref_aircraft_y3_2', 'pref_aircraft_y3_3', 'pref_aircraft_y3_4',
       'pref_aircraft_y3_5', 'pref_city_y2_1', 'dist_cnt_y3',
       'avg_dist_cnt_y2', 'avg_dist_cnt_y3', 'select_seat_cnt_y3',
       'dist_i_cnt_y2', 'dist_i_cnt_y3', 'dist_all_cnt_y2', 'dist_all_cnt_y3',
       'flt_delay_time_m3', 'flt_delay_time_m6', 'flt_delay_time_y1',
       'flt_delay_time_y2', 'pref_orig_city_y2', 'pref_orig_city_y3',
       'tkt_3y_amt', 'tkt_avg_amt_y2', 'tkt_avg_amt_y3', 'tkt_avg_interval_y3',
       'pit_all_amt', 'pit_accu_air_amt', 'pit_now_cons_amt',
       'pit_accu_amt_y3', 'pit_avg_amt_y2', 'pit_avg_amt_y3',
       'pit_avg_interval_y2', 'pit_add_chnl_y2', 'pit_add_chnl_y3']

# 创建标准化器对象
scaler = StandardScaler()

# 标准化数据
data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])
print(data)
# 保存标准化后的数据到 CSV 文件
#data.to_csv('normalized_data.csv', index=False)
# 导出清洗后的数据文件'''

