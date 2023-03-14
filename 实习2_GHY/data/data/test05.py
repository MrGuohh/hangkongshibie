# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/9 14:35

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 读取CSV文件
df = pd.read_csv('D:/实习2/data/clean_data.csv')

le = LabelEncoder()

# 将"color"列中的字符串转换为数字标签
df['seg_route_to'] = le.fit_transform(df['seg_route_to'])
df['seg_flight'] = le.fit_transform(df['seg_route_to'])
df['seg_cabin'] = le.fit_transform(df['seg_route_to'])
df['gender'] = le.fit_transform(df['seg_route_to'])
df['age'] = le.fit_transform(df['seg_route_to'])
df['residence_country'] = le.fit_transform(df['residence_country'])
df['pref_aircraft_y1_4'] = le.fit_transform(df['pref_aircraft_y1_4'])
df['pref_aircraft_y1_5'] = le.fit_transform(df['pref_aircraft_y1_5'])
df['pref_aircraft_y2_1'] = le.fit_transform(df['pref_aircraft_y2_1'])
df['pref_aircraft_y2_2'] = le.fit_transform(df['pref_aircraft_y2_2'])
df['pref_aircraft_y2_3'] = le.fit_transform(df['pref_aircraft_y2_3'])
df['pref_aircraft_y2_4'] = le.fit_transform(df['pref_aircraft_y2_4'])
df['pref_aircraft_y2_5'] = le.fit_transform(df['pref_aircraft_y2_5'])
df['pref_aircraft_y3_1'] = le.fit_transform(df['pref_aircraft_y3_1'])
df['pref_aircraft_y3_2'] = le.fit_transform(df['pref_aircraft_y3_2'])
df['pref_aircraft_y3_3'] = le.fit_transform(df['pref_aircraft_y3_3'])
df['pref_aircraft_y3_4'] = le.fit_transform(df['pref_aircraft_y3_4'])
df['pref_aircraft_y3_5'] = le.fit_transform(df['pref_aircraft_y3_5'])
df['pref_city_y2_1'] = le.fit_transform(df['pref_city_y2_1'])
df['pit_add_chnl_y3'] = le.fit_transform(df['pit_add_chnl_y3'])
df['pit_add_chnl_y2'] = le.fit_transform(df['pit_add_chnl_y2'])
df['pref_orig_city_y3'] = le.fit_transform(df['pref_orig_city_y3'])
df['pref_orig_city_y2'] = le.fit_transform(df['pref_orig_city_y2'])
df['pref_city_y2_1'] = le.fit_transform(df['pref_city_y2_1'])
df['avg_dist_cnt_y3'] = le.fit_transform(df['avg_dist_cnt_y3'])
df['select_seat_cnt_y3'] = le.fit_transform(df['select_seat_cnt_y3'])

print(df)
#保存修改后的数据集
df.to_csv("new_data.csv", index=False)
