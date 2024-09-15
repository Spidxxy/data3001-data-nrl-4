import pandas as pd 
import scipy.stats as stats

# edited PTB data from events
df = pd.read_csv('/Users/nabiharajput/Desktop/DATA3001/UNSW Data/Data Exploration/PTB_event_data.csv')

### WEATHERCONDITIONID ###

# Drop rows with missing values in either column
df_weather = df
df_weather = df_weather.dropna(subset=['WeatherConditionId', 'DurationSecs'])

# Group by 'WeatherCondition' and compute the mean of 'DurationSecs'
group_means = df_weather.groupby('WeatherConditionId')['DurationSecs'].mean()
print(group_means)

# Perform one-way ANOVA test to check for differences in 'DurationSecs' across 'WeatherCondition'
groups = [df_weather['DurationSecs'][df['WeatherConditionId'] == condition] for condition in df_weather['WeatherConditionId'].unique()]
anova_result = stats.f_oneway(*groups)

print(f"ANOVA result (F-statistic, p-value): {anova_result}")

### VenueID ###
df_venue = df

df_venue = df_venue.dropna(subset=['VenueId', 'DurationSecs'])

group_means = df_venue.groupby('VenueId')['DurationSecs'].mean()
print(group_means)

groups = [df_venue['DurationSecs'][df_venue['VenueId'] == condition] for condition in df_venue['VenueId'].unique()]
anova_result = stats.f_oneway(*groups)

print(f"ANOVA result (F-statistic, p-value): {anova_result}")

### Captain ###

df_cap = df

df_cap = df_cap.dropna(subset=['Captain', 'DurationSecs'])

group_means = df_cap.groupby('Captain')['DurationSecs'].mean()
print(group_means)

groups = [df_cap['DurationSecs'][df_cap['Captain'] == condition] for condition in df_cap['Captain'].unique()]
anova_result = stats.f_oneway(*groups)

print(f"ANOVA result (F-statistic, p-value): {anova_result}")

### MatchId ###

df_match = df

df_match = df_match.dropna(subset=['MatchId', 'DurationSecs'])

group_means = df_match.groupby('MatchId')['DurationSecs'].mean()
print(group_means)

groups = [df_match['DurationSecs'][df_match['MatchId'] == condition] for condition in df_match['MatchId'].unique()]
anova_result = stats.f_oneway(*groups)

print(f"ANOVA result (F-statistic, p-value): {anova_result}")

### SeqNumber ###

df_seq = df

df_seq = df_seq.dropna(subset=['SeqNumber', 'DurationSecs'])

group_means = df_seq.groupby('SeqNumber')['DurationSecs'].mean()
print(group_means)

groups = [df_seq['DurationSecs'][df_seq['SeqNumber'] == condition] for condition in df_seq['SeqNumber'].unique()]
anova_result = stats.f_oneway(*groups)

print(f"ANOVA result (F-statistic, p-value): {anova_result}")

# ### SeasonId ###

# df_season = df

# df_season = df_season.dropna(subset=['SeasonId', 'DurationSecs'])

# group_means = df_season.groupby('SeasonId')['DurationSecs'].mean()
# print(group_means)

# groups = [df_season['DurationSecs'][df_season['SeasonId'] == condition] for condition in df_season['SeasonId'].unique()]
# anova_result = stats.f_oneway(*groups)

# print(f"ANOVA result (F-statistic, p-value): {anova_result}")

# ### SeriesId ###

# df_series = df

# df_series = df_series.dropna(subset=['SeriesId', 'DurationSecs'])

# group_means = df_series.groupby('SeriesId')['DurationSecs'].mean()
# print(group_means)

# groups = [df_series['DurationSecs'][df_series['SeriesId'] == condition] for condition in df_series['SeriesId'].unique()]
# anova_result = stats.f_oneway(*groups)

# print(f"ANOVA result (F-statistic, p-value): {anova_result}")

### RunOn ###

df_runon = df

df_runon = df_runon.dropna(subset=['RunOn', 'DurationSecs'])

group_means = df_runon.groupby('RunOn')['DurationSecs'].mean()
print(group_means)

groups = [df_runon['DurationSecs'][df_runon['RunOn'] == condition] for condition in df_runon['RunOn'].unique()]
anova_result = stats.f_oneway(*groups)

print(f"ANOVA result (F-statistic, p-value): {anova_result}")