import pandas as pd

# Load the CSV file
file_path =(r"/Users/nabiharajput/Desktop/DATA3001/UNSW Data/2020-2023 Event Data.csv") # Replace with your CSV file path if ur working on/copying this
df = pd.read_csv(file_path)

# df = pd.read_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/2020-2023 Event Data.csv')

# filter for rows where EventName includes 'PTB OR Tackle ()'
Event_ptb_df = df[(df['EventName'].str.contains('PTB', case=False, na=False)) | (df['EventName'].str.contains('Tackle', case=False, na=False))]

Event_ptb_df.to_csv(r'/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv', index=False)