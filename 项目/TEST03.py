import pandas as pd
data = pd.read_csv('train-checkpoint.csv')

selected_data = data[['emd_lable2', 'ffp_nbr', 'seat_middle_cnt_y3',
                      'prebuy_i_cnt_y2_d99', 'prebuy_i_cnt_y3_d3', 'prebuy_i_cnt_y3_d7',
                      'prebuy_i_cnt_y3_d99', 'avg_dist_cnt_y2', 'pit_avg_amt_y2', 'pit_avg_amt_y3']]
data = selected_data.dropna()

data = selected_data.drop_duplicates()
print(data)
data.to_csv('selected_features.csv', index=False)