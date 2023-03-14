# 学校:武汉工程大学
# 学生:郭昊阳
# 开发时间:2023/3/9 15:54
import pandas as pd
df = pd.read_csv('D:/实习2/train.csv')
data=df[['pax_name', 'pax_passport', 'seg_dep_time', 'pax_fcny', 'pax_tax',
       'emd_lable', 'birth_date', 'nation_name', 'city_name', 'cabin_c_cnt_y3',
       'pref_aircraft_y1_5', 'pref_aircraft_y2_1', 'pref_aircraft_y2_2',
       'pref_aircraft_y2_3', 'pref_aircraft_y2_4', 'pref_aircraft_y2_5',
       'pref_aircraft_y3_1', 'pref_aircraft_y3_2', 'pref_aircraft_y3_3',
       'pref_aircraft_y3_4', 'pref_aircraft_y3_5', 'pref_orig_y2_4',
       'pref_orig_y3_4', 'pref_line_y1_1', 'pref_line_y1_2', 'pref_line_y1_3',
       'pref_line_y1_4', 'pref_line_y1_5', 'pref_line_y2_2', 'pref_line_y2_5',
       'pref_line_y3_2', 'pref_line_y3_5', 'pref_city_y2_1', 'pref_city_y3_1',
       'recent_flt_day', 'dist_cnt_y1', 'dist_cnt_y3', 'avg_dist_cnt_m6',
       'avg_dist_cnt_y2', 'avg_dist_cnt_y3', 'select_seat_cnt_y2',
       'select_seat_cnt_y3', 'dist_d_cnt_y1', 'dist_d_cnt_y2', 'dist_d_cnt_y3',
       'dist_i_cnt_y1', 'dist_i_cnt_y2', 'dist_i_cnt_y3', 'dist_all_cnt_y1',
       'dist_all_cnt_y2', 'dist_all_cnt_y3', 'cabin_hi_cnt_y3',
       'pref_orig_city_y2', 'pref_orig_city_y3', 'tkt_3y_amt', 'tkt_d_amt_y1',
       'tkt_d_amt_y2', 'tkt_d_amt_y3', 'tkt_i_amt_y1', 'tkt_i_amt_y2',
       'tkt_i_amt_y3', 'tkt_all_amt_m6', 'tkt_all_amt_y1', 'tkt_all_amt_y2',
       'tkt_all_amt_y3', 'tkt_avg_amt_y2', 'tkt_avg_amt_y3',
       'tkt_avg_interval_y2', 'tkt_avg_interval_y3', 'pit_all_amt',
       'pit_accu_air_amt', 'pit_accu_non_amt', 'pit_now_cons_amt',
       'pit_next_level_dist', 'mdl_influence', 'pit_accu_amt_m6',
       'pit_accu_amt_y2', 'pit_accu_amt_y3', 'pit_cons_amt_y3',
       'pit_avg_accu_amt_y2', 'pit_avg_accu_amt_y3', 'pit_avg_cons_amt_y3',
       'pit_add_air_amt_y1', 'pit_add_air_amt_y2', 'pit_add_non_amt_y3',
       'pit_des_out_amt_y2', 'pit_des_out_amt_y3', 'pit_avg_amt_y1',
       'pit_avg_amt_y2', 'pit_avg_amt_y3', 'pit_avg_interval_y1',
       'pit_avg_interval_y2', 'pit_avg_interval_y3', 'pit_ech_avg_amt_y2',
       'pit_ech_avg_amt_y3', 'pit_out_avg_amt_y2', 'pit_out_avg_amt_y3',
       'pit_income_avg_amt_y2', 'pit_income_avg_amt_y3', 'pit_pay_avg_amt_y3','emd_lable2']]
data.to_csv('first.csv', index=False)