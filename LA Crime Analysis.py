# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read and preview the dataset
# We use parse_dates to convert columns into datetime objects
# We specify the dtype of 'TIME OCC' to be treated as string 'str'
crimes = pd.read_csv(r'C:\Users\symon\Downloads\crimes.csv', parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
#print(crimes.info())

## Finding the highest frequency of crimes by hour

# Extracting first two digits of 'TIME OCC' to represent hour and change data type to integer
crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)
print(crimes.head())

# Countplot to find the largest frequency of crimes by hour
sns.countplot(data=crimes, x="HOUR OCC")
plt.show()

# Midday has the largest volume of crime
peak_crime_hour = 12

# Finding areas with largest frequency of night crimes (between 10pm to 3:59am)
night_time = crimes[crimes["HOUR OCC"].isin([22,23,0,1,2,3])]  # note: the time is in 24hr format

# Grouping by area name and count occurences filtering with largest value
peak_night_crime_location = night_time.groupby("AREA NAME",
                                               as_index=False)["HOUR OCC"].count().sort_values("HOUR OCC",
                                                                                                ascending=False).iloc[0]["AREA NAME"]

print(f"The area with the largest volume of night crime is {peak_night_crime_location}")

# Finding the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+)
# Creating bins and labels for victim age ranges
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

# Adding a new column
crimes["Age Bracket"] = pd.cut(crimes["Vict Age"],
                               bins=age_bins,
                               labels=age_labels)

# Finding the category with the largest frequency
victim_ages = crimes["Age Bracket"].value_counts()
print(victim_ages)