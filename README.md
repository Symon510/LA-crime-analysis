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


Night Crime Hotspots :
Night crimes were defined as those occurring between 10 PM and 3:59 AM.

 ![image](https://github.com/user-attachments/assets/c77512ca-a5c5-48a0-9bcf-57093341ce1b)

A subset of the dataset was filtered for these hours, and crimes were grouped by AREA NAME.

 ![image](https://github.com/user-attachments/assets/585f214d-5d30-4e2c-aa38-c162ff274e75)

The area with the largest volume of night crimes was identified as "Central".

Visualization:
(Include a bar chart or table summarizing night crime frequency by area.)
Victim Age Distribution:

Age groups were created using bins: 0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+.

 ![image](https://github.com/user-attachments/assets/d973c657-43a6-4a58-b5ee-41a786e3062e)

A new column, Age Bracket was added to classify victims into these categories.

 ![image](https://github.com/user-attachments/assets/5d4bef4f-4192-41dd-99a0-863e3267c003)

The most targeted age group was 18-25 with 500 incidents.

Visualization:

 ![Figure_2](https://github.com/user-attachments/assets/849f717b-6072-4bb2-9f59-0dae25bc5da8)

Conclusion:
This analysis provides insights into crime patterns, highlighting the most vulnerable time periods, geographic hotspots, and victim demographics. It can help authorities allocate resources more effectively and raise awareness among high-risk groups.
