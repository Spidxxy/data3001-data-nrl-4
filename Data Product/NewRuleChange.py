import pandas as pd
import numpy as np

# Load the CSV file
file_path =(r"/Users/nabiharajput/Desktop/DATA3001/UNSW Data/2020-2023 Event Data.csv") # Replace with your CSV file path if ur working on/copying this
df = pd.read_csv(file_path)

conditions = [
    (df['RoundId'] < 9) & (df['SeasonId'] == 2020),  # If RoundId < 9 and Year = 2020
    (df['SeasonId'] < 2022) & (df['RoundId'] >= 9),  # If Year < 2022 and RoundId >= 9
    (df['SeasonId'] >= 2022)                         # If Year >= 2022
]

value = [0, 1, 2]  # 0 for first condition, 1 for second, 2 for third

df['RuleChange'] = np.select(conditions, value, default=np.nan)  # Else: NA (NaN in pandas)

df.to_csv(r'/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Product/2020-2023 PTB and Tackle Filtered.csv', index=False)