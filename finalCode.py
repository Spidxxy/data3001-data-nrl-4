# code used to make final data product
    ## use this as 

import pandas as pd
import numpy as np

### Step 1: Filter rows ###
    ### Select the rows relevant to objective. ###

# read the men's NRL csv file: 2020-2023 Event Data.csv
file_path =(r"/Users/nabiharajput/Desktop/DATA3001/Final Data Product/2020-2023 Event Data.csv") # Replace with your CSV file
df = pd.read_csv(file_path)

# filter for rows where the event is either a PTB or a tackle 
    # disregard all other events
word_to_include = ['PTB', 'Tackle']
list_inclusion = '|'.join(word_to_include)
df = df[df['EventName'].str.contains(list_inclusion, case=False, na=False)]

# disregard opponent information and specific tackle types
    # (for further information/justification about exclusions refer to ReadMe)  
words_to_remove = ['tackled', 'opp', 'penalty', 'penalised', 'Ref Tackle', 'offloaded', 'misses', 'passive', 'try saves']
list_exclusion = '|'.join(words_to_remove)
df = df[~df['EventName'].str.contains(list_exclusion, case=False, na=False)]


### Step 2: Add new variables ###
    ### Create new feature columns by manipulating/using available variables ###

# create singular time columns in mm:ss format
# combine Game time columns
df['GameSecs'] = df['GameSecs'].apply(lambda x: f'{int(x):02d}')
df['GameTime'] = df['GameMins'].astype(str) + ':' + df['GameSecs']
# combine Elapsed time columns
df['ElapsedSecs'] = df['ElapsedSecs'].apply(lambda x: f'{int(x):02d}')
df['ElapsedTime'] = df['ElapsedMins'].astype(str) + ':' + df['ElapsedSecs']
# drop existing time columns
df = df.drop(columns=['ElapsedMins', 'ElapsedSecs', 'GameMins', 'GameSecs'])

# create 'NewRule' feature to account for the rule changes to the men's NRL game
    # rule change based on year and month it was implemented
    #  (for more detail about the rule change refer to ReadMe)
conditions = [
    (df['SeasonId'] == 2020) & (df['RoundId'] < 9),   # Before rule changes
    (df['SeasonId'] == 2020) & (df['RoundId'] >= 9),  # first rule change (6-again) implemented in Sep. 2020
    (df['SeasonId'] == 2021),                         
    (df['SeasonId'] >= 2022)                          # second rule change implemented in 2022
]
# 1 = 6-again rule 
# 2 = 
values = [0, 1, 1, 2]  
# add in new feature column
df['RuleChange'] = np.select(conditions, values, default=-1).astype(int)


### Step 3: Remove Variables ###
    ### Exclude variable columns that are not required for the objective.###

# list of variables to remove 
    # (for further information/justification about variables being removed refer to ReadMe) 
variables_to_remove = ['Anonymize 1PlayerId', 'Player Id', 'PositionId', 'RunOn', 'Captain', 
                       'InPossessionPlayerId', 'XmPossession', 'YmPossession', 'ZonePossession', 'ChannelPossession', 'SectionPossession',
                       'PossessionSecs', 'OppPossessionSecs', 'TotalPossessionSecs', 'MatchMinute',
                       'OfficialId',
                       'ElapsedMillisecs',
                       'Qualifier4Name', 'Qualifier5Name', 'Qualifier6Name', 'Qualifier7Name', 'Qualifier8Name', 
                       'Qualifier4', 'Qualifier5', 'Qualifier6', 'Qualifier7', 'Qualifier8',
                       'Opposition Id', 'Club Id', 'Club Name', 'Deidentified Away Club Id', 'Deidentified Away Club Name', 'Deidentified Club Home Id', 'Deidentified Club Home Name',
                       'SeasonId', 'Points', 'DistanceMs', 'TeamAId', 'TeamAPossessionSecs', 'TeamBId', 'TeamBPossessionSecs', 'SeriesId', 'WeatherConditionName']
# drop all the above variables columns
df = df.drop(columns=variables_to_remove)


### Step 4: Match PTB and tackles
    ### Match each PTB row with the tackles that caused it ### 
    ### This will result in PTB with extra feature columns that describe the characteristics of the tackles ###
    ### Also includes a new feature column with total number of tackles for each PTB ##

# Step 0.4: Remove duplicate rows from the original dataset
df.drop_duplicates(inplace=True)

# Step 4.1: Identify PTB rows and tackle rows
ptb_rows = df[df['EventName'].str.contains('PTB', case=False, na=False)].copy()
tackle_rows = df[df['EventName'].str.contains('tackle', case=False, na=False)].copy()

# Step 4.2: Group tackle rows by 'Set', 'Tackle', and 'MatchId'
    # This will give us the tackles that lead up to a certain PTB 
tackles_group = tackle_rows.groupby(['Set', 'Tackle', 'MatchId']).apply(
    # Store the tackle characteristics 
    lambda x: x[['Qualifier1', 'Qualifier2', 'Qualifier3']].values.tolist()
).reset_index(name='TackleCharacteristics')

# Step 4.3: Merge grouped tackle characteristics with PTB rows
    # Merge by joining on Set, Tackle and MatchId
merged = pd.merge(ptb_rows, tackles_group, on=['Set', 'Tackle', 'MatchId'], how='left')

# Step 4.4: Seperate TackleCharacteristics into seperate columns
    # There are three charcteristics for each tackle: tackle type, outcome and arrival
def expand_tackle_qualifiers(row, i, total_ptb_rows):
    # Print progress message to keep track of ptb rows being processed
    if i % 100 == 0:
        print(f"Processing PTB row {i + 1} out of {total_ptb_rows}")
    
    # List of tackle characteristics
    characteristics = row['TackleCharacteristics'] if isinstance(row['TackleCharacteristics'], list) else []
    
   # Create a dictionary to hold the seperate qualifier characteristics
    expanded_characteristics = {}
    
    # For each tackle, create new columns for characteristics
        # k = tackle number
        # chara = characteristic
    for ix, charac in enumerate(characteristics, start=1):
        for k in range(1, 4):
            expanded_characteristics[f'Tackle{ix}_TackleType'] = charac[0]  # Tackle Type
            expanded_characteristics[f'Tackle{ix}_TacklerOutcome'] = charac[1]  # Tackle Outcome
            expanded_characteristics[f'Tackle{ix}_TackleArrival'] = charac[2]  # Tackle Arrival
    
    # Add feature column which returns total number of tackles
    expanded_characteristics['Number of Tackles'] = len(characteristics)
    
    return expanded_characteristics

# Step 4.5: Run main function
# Store expanded rows
expanded_rows = []
# Total number of ptb rows
total_ptb_rows = len(merged)

# main function loop
for idx, row in enumerate(merged.itertuples(), start=0):
    expanded_data = expand_tackle_qualifiers(row._asdict(), idx, total_ptb_rows)
    # Combine the ptb row with the expanded qualifier columns
    row_data = {**row._asdict(), **expanded_data}
    expanded_rows.append(row_data)

# Step 4.6: Final product creation
expanded_ptb = pd.DataFrame(expanded_rows)

# drop the unnecessary column 'TackleCharacteristics'
columns_to_drop = ['TackleCharacteristics', 'Index', '_1', '_2', '_9', '_10', '_13', '_8']
expanded_ptb.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# reorder columns for readability
original_columns = df.columns.tolist()
new_columns = [col for col in expanded_ptb.columns if col not in original_columns]
final_column_order = [col for col in original_columns if col in expanded_ptb.columns] + new_columns
final = expanded_ptb[final_column_order]

# save data product
final.to_csv(r'/Users/nabiharajput/Desktop/DATA3001/Final Data Product/finaldataproduct.csv', index=False)

print("Process complete.")

