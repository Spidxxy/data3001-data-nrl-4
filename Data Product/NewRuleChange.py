import pandas as pd
import numpy as np

# Load the CSV file
file_path =(r"/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv") # Replace with your CSV file path if ur working on/copying this
df = pd.read_csv(file_path, low_memory=False)

conditions = [
    (df['SeasonId'] == 2020) & (df['RoundId'] < 9),   # If Year = 2020 and RoundId < 9
    (df['SeasonId'] == 2020) & (df['RoundId'] >= 9),  # Elif Year = 2020 and RoundId >= 9
    (df['SeasonId'] == 2021),                         # Elif Year = 2021
    (df['SeasonId'] >= 2022)                          # Elif Year >= 2022
]

values = [0, 1, 1, 2]  # 0 for first condition, 1 for second, 2 for third

df['RuleChange'] = np.select(conditions, values, default=-1).astype(int)  # Else: NA (NaN in pandas)

df.to_csv(r'/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered_newColumn.csv', index=False)
