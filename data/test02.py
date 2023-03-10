# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/8 16:39


import pandas as pd
data = pd.read_csv('D:/实习2/data/data/train.csv',encoding='gbk')

selected_data = data[['seg_route_to', 'seg_flight', 'seg_cabin', 'pax_fcny', 'emd_lable',
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
       'pit_avg_interval_y2', 'pit_add_chnl_y2', 'pit_add_chnl_y3']]
data = selected_data.dropna()


data = selected_data.drop_duplicates()
data.to_csv('selected_features.csv', index=False)
