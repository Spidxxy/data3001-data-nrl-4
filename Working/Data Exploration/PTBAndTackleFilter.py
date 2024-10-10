import pandas as pd


# Load the CSV file
file_path =(r"C:\Users\Ivy\Documents\Data3001\2020-2023 Event Data-001.csv") # Replace with your CSV file path if ur working on/copying this
df = pd.read_csv(file_path)

# filter for rows where EventName includes 'PTB OR Tackle ()'
Event_ptb_df = df[(df['EventName'].str.contains('PTB', case=False, na=False)) | (df['EventName'].str.contains('Tackle', case=False, na=False))]

Event_ptb_df.to_csv(r"C:\Users\Ivy\Data3001 Github dump\data3001-data-nrl-4\Data Exploration\2020-2023 PTB and Tackle Filtered.csv", index=False)