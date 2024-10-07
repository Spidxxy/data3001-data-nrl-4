import pandas as pd

# read csv file  
file_path =(r"/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv") # Replace with your CSV file path if ur working on/copying this
df = pd.read_csv(file_path, low_memory=False)

# remove rows with opp and reftackle and tackled
words_to_remove = ['tackled', 'opp', 'penalty', 'penalised', 'Ref Tackle']
pattern = '|'.join(words_to_remove)
df = df[~df['EventName'].str.contains(pattern, case=False, na=False)]

# combine Game time columns
df['GameSecs'] = df['GameSecs'].apply(lambda x: f'{int(x):02d}')
df['GameTime'] = df['GameMins'].astype(str) + ':' + df['GameSecs']

# combine Elapsed time columns
df['ElapsedSecs'] = df['ElapsedSecs'].apply(lambda x: f'{int(x):02d}')
df['ElapsedTime'] = df['ElapsedMins'].astype(str) + ':' + df['ElapsedSecs']

df = df.drop(columns=['ElapsedMins', 'ElapsedSecs', 'GameMins', 'GameSecs'])

df.to_csv(r'/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv', index=False)