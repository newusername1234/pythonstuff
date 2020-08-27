import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv(
    'sales_data.csv',
    parse_dates=['Date'])

# print(sales.head())
# print(sales.shape)
# print(sales.info())
# print(sales.describe())
# print(sales['Unit_Cost'].describe())
# print(sales['Unit_Cost'].mean())
# sales['Unit_Cost'].plot(kind='box',vert=False,figsize=(14,6))
# ax = sales['Unit_Cost'].plot(kind='density',figsize=(14,6))
# ax.axvline(sales['Unit_Cost'].mean(),color='red')
# ax.axvline(sales['Unit_Cost'].median(),color='green')
# ax = sales['Unit_Cost'].plot(kind='hist',figsize=(14,6))
# ax.set_ylabel('Number of Sales')
# ax.set_xlabel('dollars')
sales['Age_Group'].value_counts().plot(kind='pie',figsize=(6,6))
plt.show()