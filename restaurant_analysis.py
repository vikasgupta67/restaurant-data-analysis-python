# Restaurant Data Analysis | By Vikas Gupta
# Tools: Python, Pandas, NumPy, Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
data = pd.read_excel('data.xlsx')
country = pd.read_excel('Country-Code.xlsx')

# 2. Merge Data
df = pd.merge(data, country, on="Country Code", how="left")
print(df.shape) # (9551, 20)

# 3. Data Quality Check
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# 4. City Analysis
city_count = df['City'].value_counts()
print(city_count.head())

# 5. Franchise Analysis - Restaurants in most cities
franchise = df.groupby('Restaurant Name')['City'].nunique().sort_values(ascending=False)
print(franchise.head(10))

# 6. Table Booking Ratio
booking_yes = (df['Has Table booking'] == 'Yes').sum()
booking_no = (df['Has Table booking'] == 'No').sum()
print(f"Booking Ratio: {booking_yes/booking_no:.3f}")

# 7. Online Delivery Coverage
delivery_pct = (df['Has Online delivery'] == 'Yes').mean() * 100
print(f"Online Delivery: {delivery_pct:.2f}%")

# 8. Votes - Delivery vs Non-Delivery
print(df.groupby('Has Online delivery')['Votes'].sum())

# 9. Cuisine Analysis
df['Cuisines'] = df['Cuisines'].fillna('Unknown')
df['Cuisine_Count'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
print(f"Max Cuisines: {df['Cuisine_Count'].max()}, Min: {df['Cuisine_Count'].min()}")

# 10. Visualization - Top 10 Cities
plt.figure(figsize=(10,6))
city_count.head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Cities by Restaurant Count')
plt.ylabel('Number of Restaurants')
plt.savefig('top_cities.png')
plt.show()
