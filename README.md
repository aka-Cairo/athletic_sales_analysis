# Analysis of Athletic Sales Data

This repository contains Python code that analyzes athletic sales data. The code is structured into sections, each performing different analyses on the data.

## Data Preparation and Cleaning

The code begins by importing necessary libraries, including `pandas` for data manipulation and `Path` from `pathlib` for file path handling.

### 1. Combine and Clean the Data

The sales data for 2020 and 2021 are imported from CSV files using `pd.read_csv()` function and stored in DataFrame variables `sales_2020` and `sales_2021`. Then, these two DataFrames are combined into a single DataFrame called `combined_sales` using `pd.concat()` function. The code also performs data cleaning tasks such as checking for null values, converting data types, and resetting the index.

## Data Analysis

The code performs various analyses on the combined sales data.

### 2. Determine which Region Sold the Most Products

The code determines which region sold the most products using both `groupby` and `pivot_table` methods. It calculates the total products sold for each region, state, and city, and then displays the top 5 areas by total products sold.

### 3. Determine which Region had the Most Sales

Similarly, the code determines which region had the most sales using both `groupby` and `pivot_table` methods. It calculates the total sales for each region, state, and city, and then displays the top 5 areas by total sales.

### 4. Determine which Retailer had the Most Sales

The code determines which retailer had the most sales using both `groupby` and `pivot_table` methods. It calculates the total sales for each retailer, region, state, and city, and then displays the top 5 areas by total sales.

### 5. Determine which Retailer Sold the Most Women's Athletic Footwear

The code filters the sales data to get women's athletic footwear sales data and then determines which retailer sold the most women's athletic footwear using both `groupby` and `pivot_table` methods.

### 6. Determine the Day with the Most Women's Athletic Footwear Sales

The code creates a pivot table with the 'invoice_date' column as the index and the "total_sales" as the values to determine the day with the most women's athletic footwear sales. It also resamples the pivot table into daily bins and sorts the resampled pivot table in ascending order on "Total Sales".

### 7. Determine the Week with the Most Women's Athletic Footwear Sales

Similarly, the code resamples the pivot table into weekly bins to determine the week with the most women's athletic footwear sales and sorts the resampled pivot table in ascending order on "Total Sales".

These analyses provide insights into sales trends and help in making informed business decisions.
