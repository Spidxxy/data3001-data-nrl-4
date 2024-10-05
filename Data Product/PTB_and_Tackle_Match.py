import pandas as pd

# read csv file  
file_path =(r"/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv") # Replace with your CSV file path if ur working on/copying this
df = pd.read_csv(file_path, low_memory=False)

# Step 1: Identify PTB rows
ptb_rows = df[df['EventName'].str.contains('PTB', case=False, na=False)].copy()

# Create columns to store tackle qualifiers dynamically
max_tackles = 0

# Step 2: For each PTB row, find matching tackle rows
for i, ptb_row in ptb_rows.iterrows():
    set_val = ptb_row['Set']
    tackle_val = ptb_row['Tackle']
    match_id = ptb_row['MatchId']
    
    # Find rows where EventName contains 'tackle' and Set, Tackle, and MatchId match
    matching_tackles = df[
        (df['EventName'].str.contains('tackle', case=False, na=False)) & 
        (df['Set'] == set_val) & 
        (df['Tackle'] == tackle_val) & 
        (df['MatchId'] == match_id)
    ]
    
    num_tackles = len(matching_tackles)
    max_tackles = max(max_tackles, num_tackles)
    
    # Append tackle qualifiers to PTB row
    for j, (idx, tackle_row) in enumerate(matching_tackles.iterrows(), start=1):
        for k in range(1, 4):
            ptb_rows.at[i, f'Tackle{j}_QualifierName{k}'] = tackle_row[f'Qualifier{k}Name']
            ptb_rows.at[i, f'Tackle{j}_Qualifier{k}'] = tackle_row[f'Qualifier{k}']
    
    # Add the number of tackles to the PTB row
    ptb_rows.at[i, 'Number of Tackles'] = num_tackles

# Step 3: Drop the tackle rows
df_cleaned = df[~df['EventName'].str.contains('tackle', case=False, na=False)]

# Step 4: Append updated PTB rows back into the cleaned dataframe
new_dataset = ptb_rows.copy()

# Save the updated DataFrame to a new CSV file
new_dataset.to_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv', index=False)