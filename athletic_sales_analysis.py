# Import Libraries and Dependencies
import pandas as pd
from pathlib import Path


# ### 1. Combine and Clean the Data
# #### Import CSVs
# Read the CSV files into DataFrames.
sales_2020_path = Path("Resources/athletic_sales_2020.csv")
sales_2021_path = Path("Resources/athletic_sales_2021.csv")

sales_2020 = pd.read_csv(sales_2020_path)
sales_2021 = pd.read_csv(sales_2021_path)


# Display the 2020 sales DataFrame
sales_2020


# Display the 2021 sales DataFrame
sales_2021


# #### Check the data types of each DataFrame
# Check the 2020 sales data types.
sales_2020.dtypes
# Check the 2021 sales data types.
sales_2020.dtypes


# #### Combine the sales data by rows.
# Combine the 2020 and 2021 sales DataFrames on the rows
combined_sales = pd.concat([sales_2020, sales_2021], axis="rows", join="inner")

# Reset the index
combined_sales.reset_index()

# Display the combined DataFrame
combined_sales

# Check if any values are null.
combined_sales.isnull().any()

# Check the data type of each column
combined_sales.dtypes

# Convert the "invoice_date" to a datetime datatype
combined_sales['invoice_date'] = pd.to_datetime(combined_sales['invoice_date'])

# Confirm that the "invoice_date" data type has been changed.
combined_sales.dtypes


# ### 2. Determine which Region Sold the Most Products

# #### Using `groupby`
# Show the number products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".

# Group the combined DataFrame by 'region', 'state', and 'city', and sum the number of products sold
grouped_sales = combined_sales.groupby(['region', 'state', 'city']).agg({'units_sold': 'sum'})

# Rename the sum to "Total_Products_Sold"
grouped_sales.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)

# Display the Top 5 areas by Total_Products_Sold
grouped_sales.sort_values(by='Total_Products_Sold', ascending=False).head(5)                           


# #### Using `pivot_table`
# Show the number products sold for region, state, and city.
# Create a pivot table to show the number of products sold for region, state, and city
pivot_table_sales = pd.pivot_table(combined_sales, 
                                   values='units_sold', 
                                   index=['region', 'state', 'city'], 
                                   aggfunc='sum')

# Rename the "units_sold" column to "Total_Products_Sold"
pivot_table_sales = pivot_table_sales.rename(columns={'units_sold': 'Total_Products_Sold'})

# Show the top 5 results.
pivot_table_sales.sort_values(by='Total_Products_Sold', ascending=False).head(5)


### 3. Determine which Region had the Most Sales

#### Using `groupby`
# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total_Sales"
# Group the combined DataFrame by 'region', 'state', and 'city', and sum the number of products sold
groupby_mostsales = combined_sales.groupby(['region', 'state', 'city']).agg({'total_sales': 'sum'})

# Rename the sum to "Total_Sales"
groupby_mostsales.rename(columns={'total_sales': 'Total_Sales'}, inplace=True)

# Display the Top 5 areas by Total_Sales
groupby_mostsales.sort_values(by='Total_Sales', ascending=False).head(5)  


#### Using `pivot_table`
# Show the total sales for the products sold for each region, state, and city.
pivot_table_most_sales = pd.pivot_table(combined_sales, 
                                   values='total_sales', 
                                   index=['region', 'state', 'city'], 
                                   aggfunc='sum')

# Rename the "units_sold" column to "Total_Products_Sold"
pivot_table_most_sales = pivot_table_most_sales.rename(columns={'total_sales': 'Total_Sales'})

# Show the top 5 results.
pivot_table_most_sales.sort_values(by='Total_Sales', ascending=False).head(5)


### 4. Determine which Retailer had the Most Sales

#### Using `groupby`
# Show the total sales for the products sold for each retailer, region, state, and city.
# Rename the "total_sales" column to "Total Sales"
# Show the top 5 results.
# Group the combined DataFrame by 'region', 'state', and 'city', and sum the number of products sold
groupby_retailersales = combined_sales.groupby(['retailer','region', 'state', 'city']).agg({'total_sales': 'sum'})

# Rename the sum to "Total_Sales"
groupby_retailersales.rename(columns={'total_sales': 'Total_Sales'}, inplace=True)

# Display the Top 5 areas by Total_Sales
groupby_retailersales.sort_values(by='Total_Sales', ascending=False).head(5)


#### Using `pivot_table`
# Show the total sales for the products sold for each retailer, region, state, and city.
pivot_table_retailersales = pd.pivot_table(combined_sales, 
                                   values='total_sales', 
                                   index=['retailer','region', 'state', 'city'], 
                                   aggfunc='sum')

# Rename the "units_sold" column to "Total_Products_Sold"
pivot_table_retailersales = pivot_table_retailersales.rename(columns={'total_sales': 'Total_Sales'})

# Show the top 5 results.
pivot_table_retailersales.sort_values(by='Total_Sales', ascending=False).head(5)


### 5. Determine which Retailer Sold the Most Women's Athletic Footwear
# Filter the sales data to get the women's athletic footwear sales data.
womens_footwear_sales = combined_sales[combined_sales['product'] == "Women's Athletic Footwear"]

#### Using `groupby`
womenathlet_groupby_units = womens_footwear_sales.groupby(['retailer','region', 'state', 'city']).agg({'units_sold': 'sum'})

# Rename the sum to "Womens_Footwear_Units_Sold"
womenathlet_groupby_units.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'}, inplace=True)

# Display the Top 5 areas by Total_Sales
womenathlet_groupby_units.sort_values(by='Womens_Footwear_Units_Sold', ascending=False).head(5)

#### Using `pivot_table`
# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
womenathlet_pivot_units = pd.pivot_table(womens_footwear_sales, 
                                   values='units_sold', 
                                   index=['retailer','region', 'state', 'city'], 
                                   aggfunc='sum')

# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
womenathlet_pivot_units = womenathlet_pivot_units.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})

# Show the top 5 results.
womenathlet_pivot_units.sort_values(by='Womens_Footwear_Units_Sold', ascending=False).head(5)


### 5. Determine the Day with the Most Women's Athletic Footwear Sales
# Create a pivot table with the 'invoice_date' column as the index, and the "total_sales" as the values.
pivot_table_womens_sales = pd.pivot_table(womens_footwear_sales, 
                                          values='total_sales', 
                                          index='invoice_date', 
                                          aggfunc='sum')
# Optional: Rename the "total_sales" column to "Total Sales"
pivot_table_womens_sales = pivot_table_womens_sales.rename(columns={'total_sales': 'Total Sales'})
# Show the table.
pivot_table_womens_sales

# Resample the pivot table into daily bins, and get the total sales for each day.
daily_sales = pivot_table_womens_sales.resample('D').sum()

# Sort the resampled pivot table in ascending order on "Total Sales".
daily_sales_sorted = daily_sales.sort_values(by='Total Sales', ascending=True)
daily_sales_sorted

### 6.  Determine the Week with the Most Women's Athletic Footwear Sales
# Resample the pivot table into weekly bins, and get the total sales for each week.
weekly_sales = pivot_table_womens_sales.resample('W').sum()

# Sort the resampled pivot table in ascending order on "Total Sales".
weekly_sales_sorted = weekly_sales.sort_values(by='Total Sales', ascending=True)
weekly_sales_sorted