import pandas as pd 

df = pd.read_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Exploration/PTB_event_data.csv')

average_duration = df.groupby('EventName')['DurationSecs'].mean()

print(average_duration)