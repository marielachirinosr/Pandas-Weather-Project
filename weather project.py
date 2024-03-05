import pandas as pd

# Read the weather data
weather_file = pd.read_csv('weather.csv')

# Display basic information about the data
print("Shape:", weather_file.shape)
print("Index:", weather_file.index)
print("Columns:", weather_file.columns)
print("Data Types:\n", weather_file.dtypes)
print("Head:\n", weather_file.head())
print("Unique Values in 'Weather':", weather_file['Weather'].unique())
print("Number of Unique Values:", weather_file.nunique())
print("Count per Column:\n", weather_file.count())
print("Value Counts for 'Weather':\n", weather_file['Weather'].value_counts())
print("Info:\n", weather_file.info())

# Find all the unique 'Wind Speed' values in the data
weather_file_nunique = weather_file['Wind Speed_km/h'].nunique()
weather_file_unique = weather_file['Wind Speed_km/h'].unique()

print("Wind Speed Unique Count:", weather_file_nunique)
print("Wind Speed Unique Values:", weather_file_unique)

# Find the number of times when the "Weather is exactly Clear"
clear_counts = weather_file['Weather'].value_counts()
print("Clear Weather Counts:\n", clear_counts)

filtered_weather_file = weather_file[weather_file['Weather'] == 'Clear']
print("Filtered Weather (Clear):\n", filtered_weather_file)

grouped_data = filtered_weather_file.groupby('Weather').get_group('Clear')
print("Total Value of Clear Weather:\n", grouped_data)

# Find the number of times when the 'Wind Speed was exactly 4 km/h'
filtered_weather_file_wind_4 = weather_file[weather_file['Wind Speed_km/h'] == 4]
print("Filtered Wind Speed (4 km/h):\n", filtered_weather_file_wind_4)

# Find out all the Null Values in the data
null_values = weather_file.notnull()
print("Null Values:\n", null_values)

null_count_per_column = weather_file.isnull().sum()
print("Null Value Count per Column:\n", null_count_per_column)

# Rename the column name 'Weather' of the dataframe to 'Weather Condition'
renamed_weather_file = weather_file.rename(columns={"Weather": "Weather Condition"})
print("Renamed DataFrame:\n", renamed_weather_file)

# What is the mean 'Visibility'
mean_visibility = weather_file['Visibility_km'].mean()
print("Mean Visibility_km:", mean_visibility)

# What is the Standard Deviation of 'Pressure' in this data
std_pressure = weather_file['Press_kPa'].std()
print("Standard Deviation of Pressure:", std_pressure)

# What is the Variance of 'Relative Humidity' in this data
var_relative_humidity = weather_file['Rel Hum_%'].var()
print("Variance of column 'Rel Hum_%':", var_relative_humidity)

# Find all instances when 'Snow' was recorded.
snow_weather_counts = renamed_weather_file['Weather Condition'].value_counts()
snow_instances = renamed_weather_file[renamed_weather_file['Weather Condition'].str.contains('Snow')]
print("Snow Instances:\n", snow_instances)

# Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
filtered_instances_wind_24_visibility_25 = weather_file[
    (weather_file['Wind Speed_km/h'] > 24) & (weather_file['Visibility_km'] == 25)
]
print("Filtered Instances (Wind Speed > 24 and Visibility == 25):\n", filtered_instances_wind_24_visibility_25)

# What is the Mean value of each column against each 'Weather Condition'?
numeric_columns = weather_file.select_dtypes(include='number')
mean_by_weather = numeric_columns.groupby(weather_file['Weather']).mean()

fog =  weather_file[weather_file['Weather'] == "Fog"]
numeric_columns_fog = fog.select_dtypes(include="number").mean()

print("Mean by Weather Condition:\n", mean_by_weather)
print('Mean in Fog: ', numeric_columns_fog)
filtered_rows_fog = mean_by_weather[mean_by_weather.index == "Fog"]
print('Fog General')
print(filtered_rows_fog)
print('Fog')
print(numeric_columns_fog)

# What is the Minimum & Maximum value of each column against each 'Weather Condition'?
max_by_weather = numeric_columns.groupby(weather_file['Weather']).max()
min_by_weather = numeric_columns.groupby(weather_file['Weather']).min()

print("Maximum Values by Weather Condition:\n", max_by_weather)
print("Minimum Values by Weather Condition:\n", min_by_weather)

# Show all the Records where Weather Condition is Fog.
filtered_weather_fog = weather_file[weather_file['Weather'] == 'Fog']
print("Filtered Weather (Fog):\n", filtered_weather_fog)

# Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
filtered_instances_clear_a = weather_file[
    (weather_file['Weather'] == 'Clear') | (weather_file['Visibility_km'] > 40)
]
print("Filtered Instances (Clear or Visibility > 40):\n", filtered_instances_clear_a)

# Find all instances when : A: 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or B: 'Visibility is above 40'
filtered_instances_clear_b = weather_file[
    (weather_file['Weather'] == 'Clear') & ((weather_file['Rel Hum_%'] > 50) | (weather_file['Visibility_km'] > 40))
]
print("Filtered Instances (Clear and (Rel Hum > 50 or Visibility > 40)):\n", filtered_instances_clear_b)