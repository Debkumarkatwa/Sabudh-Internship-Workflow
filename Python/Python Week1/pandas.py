import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

'''
1.  Load the dataset into a Pandas DataFrame and display the first 5 rows to get an idea of the data. 
'''
main = pd.read_csv('/content/sample_data/Sport car price.csv')
data = pd.DataFrame(main)

data.head(5)

data.info()

'''
2.  Use Pandas to clean the dataset by removing any missing or duplicate values, and converting any non-numeric data to numeric data where appropriate. 
'''
data.dropna(inplace=True)  # Remove missing values
data.drop_duplicates(inplace=True, keep='last')  # Remove duplicate rows
data.info()

# Convert 'Price (in USD)' to numeric
data['Price (in USD)'] = data['Price (in USD)'].apply(lambda x: x.replace(',', '')).astype(float)
data.info()

# Convert '0-60 MPH Time' to numeric
data['0-60 MPH Time (seconds)'] = data['0-60 MPH Time (seconds)'].str.replace('<', '').astype(float)  # Convert 0-60 MPH Time to numeric
data.info()

# Convert 'Torque (lb-ft)' to numeric
data['Torque (lb-ft)'] = data['Torque (lb-ft)'].str.replace('-', '0').str.replace('+', '').str.replace(',', '').astype(int)
data.info()

# Convert 'Horsepower' to numeric
data['Horsepower'] = data['Horsepower'].str.replace(',', '').str.replace('+', '').astype(int)
data.info()

# for column in data.columns:
#     print(data[column].value_counts())
#     print("-"*50)
print(data[data.columns[-5]].unique())

# Creating new coloum of 0 & 1 for Electric
data['Electric'] = data['Engine Size (L)'].copy()
data['Electric'] = data['Electric'].apply(lambda x : 0 if 'Electric' not in str(x) else 1)  # 0 = 'NO' 1 = 'YES'
data.info()

# Creating new coloum of 0 & 1 for Hybrid
data['Hybrid'] = data['Engine Size (L)'].copy()
data['Hybrid'] = data['Hybrid'].apply(lambda x : 0 if 'Hybrid' not in str(x) else 1)  # 0 = 'NO' 1 = 'YES'
data.info()

data.reset_index(drop=True, inplace=True)
data.info()

data.head(10)

# Remove the electric and hybrid values from Engine size
data['Engine Size (L)'] = data['Engine Size (L)'].apply(lambda x : x if len(str(x)) == 1 else re.search('\d{1}\.\d{1}', str(x)))
data['Engine Size (L)'] = data['Engine Size (L)'].apply(lambda x : x.group() if type(x) == re.Match else x)
data['Engine Size (L)'] = data['Engine Size (L)'].str.replace('-', '').str.replace('', '0').astype(float)
data.info()

'''
3.  Use Pandas to explore the dataset by computing summary statistics for each column, such as mean, median, mode, standard deviation, and range.
'''
summary_stats = data.describe()  # Compute summary statistics
print(summary_stats)

'''
4.  Use Pandas to group the dataset by car make and compute the average price for each make.
'''
average_price_by_make = data.groupby('Car Make')['Price (in USD)'].mean().reset_index()
print(average_price_by_make)

'''
5.  Use Pandas to group the dataset by year and compute the average horsepower for each year.
'''
average_horsepower_by_year = data.groupby('Year')['Horsepower'].mean().reset_index()
print(average_horsepower_by_year)

'''
6.  Use Pandas to create a scatter plot of price versus horsepower, and add a linear regression line to the plot.
'''
plt.figure(figsize=(10, 6))
sns.regplot(x='Horsepower', y='Price (in USD)', data=data, scatter_kws={'s': 10}, line_kws={'color': 'red'})
plt.title('Price vs Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('Price (in USD)')
plt.show()

'''
7.  Use Pandas to create a histogram of the 0-60 MPH times in the dataset, with bins of size 0.5 seconds.
'''
plt.figure(figsize=(10, 6))
sns.histplot(data['0-60 MPH Time (seconds)'], bins=range(0, int(data['0-60 MPH Time (seconds)'].max()) + 1, 1), kde=False)
plt.title('Histogram of 0-60 MPH Times')
plt.xlabel('0-60 MPH Time (seconds)')
plt.ylabel('Frequency')
plt.show()

'''
8.  Use Pandas to filter the dataset to only include cars with a price greater than $500,000, and then sort the resulting dataset by horsepower in descending order.
'''
filtered_cars = data[data['Price (in USD)'] > 500000].sort_values(by='Horsepower', ascending=False)
print(filtered_cars)

'''
9.  Use Pandas to export the cleaned and transformed dataset to a new CSV file.
'''
data.to_csv(r'D:\A\Shubhud\Python\Python Week1\Cleaned_Sport_Car_Price.csv', index=False)