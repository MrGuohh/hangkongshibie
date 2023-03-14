import pandas as pd
data = pd.read_csv('test.csv')

selected_data = data[['pax_name','pax_tax', 'pax_fcny', 'avg_dist_cnt_m3',
                      'seg_flight', 'tkt_3y_amt', 'dist_cnt_y3',
                      'dist_i_cnt_y3', 'seat_walkway_cnt_y3', 'flt_bag_cnt_y1', 'dist_i_cnt_y2',
                      'pref_month_m3_1','seg_route_to','avg_dist_cnt_m6','tkt_avg_amt_y3','emd_lable2']]
data = selected_data.dropna()

data = selected_data.drop_duplicates()
print(data)
data.to_csv('test_train.csv', index=False)