import pandas as pd
import os

def get_base_data():
    dir = "csse_covid_19_daily_reports_us"
    data_list = os.listdir(dir)
    data21 = [data for data in data_list if data[6:] == '2021.csv']
    data21_len = len(data21)
    print(data21)
    print("=" * 100)
    dframe = None
    for i in range(data21_len - 1):
        pre_frame = pd.read_csv(dir + '/' + data21[i])
        next_frame = pd.read_csv(dir + '/' + data21[i + 1])
        confimed_sub = next_frame['Confirmed'] - pre_frame['Confirmed']
        death_sub = next_frame['Deaths'] - pre_frame['Deaths']
        recovered_sub = next_frame['Recovered'] - pre_frame['Recovered']
        next_frame['Confirmed'] = confimed_sub
        next_frame['Deaths'] = death_sub
        next_frame['Recovered'] = death_sub
        if dframe is None:
            dframe = next_frame
        else:
            dframe = pd.concat([dframe, next_frame], ignore_index=True)
    save_dframe = dframe[['Province_State','Confirmed','Deaths','Recovered','Lat','Long_']]
    save_dframe.to_csv("data.csv")
    dframe.to_csv("first_data.csv")

get_base_data()









