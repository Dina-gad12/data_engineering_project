# importing libraries
import numpy as np
import pandas as pd

# reading the file
df = pd.read_csv("C:\\Users\\Dina Gad\\sales_data_assignment.csv")

# data_preview
print('\n', 'data_preview', '\n', df.head())
print(df.tail())

# data_summary
print('\n\n', df.info())
print('\n', df.describe())
print('\n', df.isna().sum())
print('\n', df.isna())

# checking unique shipping company
print('\n\n', 'unique_shipping_company', '\n')
print(df['shipping_company'].value_counts())

# checking duplicates
duplicates = df.duplicated()
print("duplicated_data :", duplicates.sum())

# Data cleaning
# converting dates
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['shipping_date'] = pd.to_datetime(df['shipping_date'], errors='coerce')

# shipping_cost
df['shipping_cost'] = pd.to_numeric(df['shipping_cost'], errors='coerce')
# any value less thanzero (negative) consider it NAN
df.loc[df['shipping_cost'] < 0, 'shipping_cost'] = np.nan

# Handling Nulls in another colums
# df['order_id'] = df['order_id'].fillna(method='ffill') #no nulls in order_id
df['shipping_city'] = df['shipping_city'].fillna('unkown')
df['shipping_company'] = df['shipping_company'].fillna("unspecified")

# standarizing names
df['shipping_country'] = df['shipping_country'].str.strip().str.title()
df['shipping_city'] = df['shipping_city'].str.title()
df['shipping_company'] = df['shipping_company'].str.strip().str.title()
print(df.head())

# feature engineering
# 1- days between orders and shippment  | delivery staus (unkown/late/ontime)

# converting the timedelta to numbers
df['delivery_days'] = (df['shipping_date'] - df['order_date']).dt.days


def get_status(x):
    if pd.isna(x):
        return "unkown"  # if the delivry time is null return unkown
    elif x > 11:
        return "late"
    else:
        return "ontime"


print('\n\n', 'with_delivey_col', '\n\n', df.head())
df['delivery_status'] = df['delivery_days'].apply(get_status)
print('\n\n', 'with_delivery_status ', '\n\n', df.head())

# check shipping company if domestic or international


def check_domestic(country):
    if country in domestic_countries:
        return 'yes'
    else:
        return 'No'


domestic_countries = ['Jordon']
df['is_domestic'] = df['shipping_country'].apply(check_domestic)
print('\n\n', 'domestic_status', '\n', df.head())

# Grouping
# calculate the avg shipping cost by company
avg_shipping_cost_by_company = df.groupby('shipping_company')[
    'shipping_cost'].mean().round()
print('\n\n', 'avg_shipping_cost_by_company :')
print('\n', avg_shipping_cost_by_company)

# exporting final data file
df.to_csv(("cleaned_final_data.csv"), index=False)

# data breakdown (reporting)
# 1- delivery status breakdown (how many orders are late/ontime/unkown)
delivery_status_breakdown = df['delivery_status'].value_counts()
print('\n', 'delivery_status_breakdown :', '\n', delivery_status_breakdown)

# how many orders from a specific city\country
orders_by_country = df['shipping_country'].value_counts()
print('\n\n', orders_by_country)

orders_by_city = df['shipping_city'].value_counts()
print('\n\n', orders_by_city)
