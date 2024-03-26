# Import Libraries and Dependencies
import pandas as pd
from pathlib import Path


# ### 1. Combine and Clean the Data
# #### Import CSVs

# In[2]:


# Read the CSV files into DataFrames.
sales_2020_path = Path("Resources/athletic_sales_2020.csv")
sales_2021_path = Path("Resources/athletic_sales_2021.csv")

sales_2020 = pd.read_csv(sales_2020_path)
sales_2021 = pd.read_csv(sales_2021_path)


# In[3]:


# Display the 2020 sales DataFrame
sales_2020


# In[4]:


# Display the 2021 sales DataFrame
sales_2021


# #### Check the data types of each DataFrame

# In[5]:


# Check the 2020 sales data types.
sales_2020.dtypes


# In[6]:


# Check the 2021 sales data types.
sales_2020.dtypes


# #### Combine the sales data by rows.

# In[7]:


# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index.

# Combine the 2020 and 2021 sales DataFrames on the rows
combined_sales = pd.concat([sales_2020, sales_2021], axis="rows", join="inner")

# Reset the index
combined_sales.reset_index()

# Display the combined DataFrame
combined_sales


# In[8]:


# Check if any values are null.
combined_sales.isnull().any()


# In[9]:


# Check the data type of each column
combined_sales.dtypes


# In[10]:


# Convert the "invoice_date" to a datetime datatype
combined_sales['invoice_date'] = pd.to_datetime(combined_sales['invoice_date'])


# In[11]:


# Confirm that the "invoice_date" data type has been changed.
combined_sales.dtypes



# ### 2. Determine which Region Sold the Most Products

# #### Using `groupby`

# In[12]:


# Show the number products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".

# Group the combined DataFrame by 'region', 'state', and 'city', and sum the number of products sold
grouped_sales = combined_sales.groupby(['region', 'state', 'city']).agg({'units_sold': 'sum'})

# Rename the sum to "Total_Products_Sold"
grouped_sales.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)

# Show the top 5 results.  TOP FIVE WHAT????  There are only 5 regions total.
#################
# Group the combined DataFrame by 'region' and sum the number of products sold
region_sales = combined_sales.groupby('region')['units_sold'].sum()

# Sort the regions by the total number of products sold in descending order
sorted_region_sales = region_sales.sort_values(ascending=False)

# Display the regions from most sold to least
print("Regions from most sold to least:")
print(sorted_region_sales)

                            


# #### Using `pivot_table`

# In[13]:


# Show the number products sold for region, state, and city.
# Create a pivot table to show the number of products sold for region, state, and city
pivot_table_sales = pd.pivot_table(combined_sales, 
                                   values='units_sold', 
                                   index=['region', 'state', 'city'], 
                                   aggfunc='sum')

# Rename the "units_sold" column to "Total_Products_Sold"
pivot_table_sales = pivot_table_sales.rename(columns={'units_sold': 'Total_Products_Sold'})

# Display the pivot table with the renamed column
print("Number of products sold for region, state, and city with renamed column:")
print(pivot_table_sales)

# Show the top 5 results.


# ### 3. Determine which Region had the Most Sales

# #### Using `groupby`

# In[14]:


# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.


# #### Using `pivot_table`

# In[15]:


# Show the total sales for the products sold for each region, state, and city.


# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.


# ### 4. Determine which Retailer had the Most Sales

# #### Using `groupby`

# In[16]:


# Show the total sales for the products sold for each retailer, region, state, and city.
# Rename the "total_sales" column to "Total Sales"

# Show the top 5 results.


# #### Using `pivot_table`

# In[17]:


# Show the total sales for the products sold for each retailer, region, state, and city.


# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.


# ### 5. Determine which Retailer Sold the Most Women's Athletic Footwear

# In[18]:


# Filter the sales data to get the women's athletic footwear sales data.


# #### Using `groupby`

# In[19]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"

# Show the top 5 results.


# #### Using `pivot_table`

# In[20]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.


# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"

# Show the top 5 results.


# ### 5. Determine the Day with the Most Women's Athletic Footwear Sales

# In[21]:


# Create a pivot table with the 'invoice_date' column is the index, and the "total_sales" as the values.


# Optional: Rename the "total_sales" column to "Total Sales"


# Show the table.


# In[22]:


# Resample the pivot table into daily bins, and get the total sales for each day.


# Sort the resampled pivot table in ascending order on "Total Sales".


# ### 6.  Determine the Week with the Most Women's Athletic Footwear Sales

# In[23]:


# Resample the pivot table into weekly bins, and get the total sales for each week.


# Sort the resampled pivot table in ascending order on "Total Sales".


# In[ ]:




