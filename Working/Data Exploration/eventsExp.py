import pandas as pd

# read event file
df = pd.read_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/2021 Event Data.csv')

# filter for rows where EventName includes 'PTB'
ptb_df = df[df['EventName'].str.contains('PTB', case=False, na=False)]

# save file
ptb_df.to_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Exploration/PTB_event_data.csv', index=False)
