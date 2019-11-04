"""Python for Data Science - Perform Data Science on Titanic Dataset
a)Load the Titanic dataset into one of the data structures (NumPy or Pandas).
b)Display header rows and description of the loaded dataset.
c) Remove unnecessary features (E.g. drop unwanted columns) from the dataset.
d) Manipulate data by replacing empty column values with a default value.
e) Perform the following visualizations on the loaded dataset:
     i)   Passenger status (Survived/Died) against Passenger Class
     ii)  Survival rate of male vs female
     iii) No of passengers in each age group


#numpy - Deals multi-dimensional arrays and matrices
#seaborn - Deals with data visualization
#matplotlib - Plotting; pyplot-interactive plotting
#pandas - data structures and data analysis tools"""
#import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

weather_df = pd.read_csv('weather.csv')


# print("======Data Headers Before Dropping Columns=======")
# print(titanic_df.head(5))

print("**** \n\nDATA TRANSFORMATION *****\n")

print("======Data Headers After Dropping Columns - First Way=======")
weather_df.drop(['Formatted Date','Wind Speed (km/h)','Daily Summary', 'Loud Cover', 'Wind Bearing (degrees)', 'Precip Type', 'Apparent Temperature (C)', 'Pressure (millibars)', 'Summary'], axis=1, inplace=True)
#axis =1 in drop method shows you are dropping a column
#inplace=True means you are editing original dataframe
print(weather_df.head(5))

print("\n\n\n**** DATA VISUALIZATIONS****\n\n")
print("Visualization #1 : Humidity vs Visibility")
ax = sns.countplot(x = 'Humidity', hue = 'Visibility (km)', palette = 'Set1',data = weather_df)
ax.set(title = 'Humidity against Visibility',
       xlabel = 'Humidity', ylabel = 'Visibility')
plt.show()   

# #crosstab - Cross tabulation of two or more factors
# print("Visualization #2 : Survival Rate Based on Gender")
# print(pd.crosstab(titanic_df["Sex"],titanic_df.Survived))
# ax = sns.countplot(x = 'Sex', hue = 'Survived', palette = 'Set2', data = titanic_df)
# ax.set(title = 'Total Survivors According to Sex', xlabel = 'Sex', ylabel='Total')
# plt.show()

# print("Visualization #3 : Survival Rate Based on Passenger Age Group")
# # We look at Age column and set Intevals on the ages and the map them to their categories as
# # (Children, Teen, Adult, Old)
# interval = (0,18,35,60,120)
# categories = ['Children','Teens','Adult', 'Old']
# #cut - Segment and sort data values into bins
# titanic_df['Age_cats'] = pd.cut(titanic_df.Age, interval, labels = categories)

# ax = sns.countplot(x = 'Age_cats',  data = titanic_df, hue = 'Survived', palette = 'Set3')

# ax.set(xlabel='Age Categorical', ylabel='Total',
#        title="Age Categorical Survival Distribution")
# plt.show()

# print("Visualization #4 : Survival Rate Based on Passenger Embarked Port")
# print(pd.crosstab(titanic_df['Embarked'], titanic_df.Survived))
# ax = sns.countplot(x = 'Embarked', hue = 'Survived', palette = 'Set1', data = titanic_df)
# ax.set(title = 'Survival distribution according to Embarking place')
# plt.show()
