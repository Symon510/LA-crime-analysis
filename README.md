# LA-crime-analysis

Overview : This repository explores a dataset of crime incidents to identify patterns in crime timings, geographic hotspots and victim age groups. The analysis focuses on finding the peak crime hours, the area with the highest volume of night crimes and the age brackets most frequently targeted.

Data Preparation :
The dataset was loaded using pandas, with date columns (Date Rptd and DATE OCC) parsed into datetime objects.
The TIME OCC column was treated as a string to extract the hour of occurrence (HOUR OCC), converted into an integer for analysis.

 ![image](https://github.com/user-attachments/assets/05c1ba72-2528-4022-bd7b-57cf0494a354)


Data Analysis:

Peak Crime Hours : The first two digits of the TIME OCC field were extracted to represent the hour crimes occurred.
A countplot revealed midday (12 PM) as the peak hour for crimes.

![image](https://github.com/user-attachments/assets/0b941c39-ddf8-4bbf-989b-9a973f859753)


Visualization:

![Figure_1](https://github.com/user-attachments/assets/f23fa36f-14e7-4288-bf86-3b5d2aea7a9a)



Night Crime Hotspots:

Night crimes were defined as those occurring between 10 PM and 3:59 AM.
A subset of the dataset was filtered for these hours, and crimes were grouped by AREA NAME.
The area with the largest volume of night crimes was identified as [Insert Area Name].
Visualization:
(Include a bar chart or table summarizing night crime frequency by area.)
Victim Age Distribution:

Age groups were created using bins: 0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+.
A new column, Age Bracket, was added to classify victims into these categories.
The most targeted age group was [Insert Age Bracket] with [Insert Count] incidents.
Visualization:
(Include a bar chart or pie chart of victim frequency by age group.)

Conclusion:
This analysis provides insights into crime patterns, highlighting the most vulnerable time periods, geographic hotspots, and victim demographics. It can help authorities allocate resources more effectively and raise awareness among high-risk groups.
