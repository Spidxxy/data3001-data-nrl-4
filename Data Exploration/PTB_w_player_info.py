import pandas as pd 

ptb_data = pd.read_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Exploration/PTB_event_data.csv')

players_data = pd.read_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Players.csv')

# merge the two files by PlayerID
merged_df = pd.merge(ptb_data, players_data, on='PlayerId', how='left')

# save new file 
merged_df.to_excel('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Exploration/events_with_playerinfo.xlsx', index=False)

