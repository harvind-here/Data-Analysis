import pandas as pd

# Load the sales data from the CSV file
sales_data = pd.read_csv("sales_data.csv")

# Group the data by category and calculate the total sales for each category
category_sales = sales_data.groupby('Category')['Sales'].sum()

# Calculate the percentage of sales for each product within its category
sales_data['Sales Percentage'] = sales_data.apply(lambda row: round((row['Sales'] / category_sales[row['Category']]) * 100, 2), axis=1)

# Save the output to a new CSV file
output_file = "HarvindMukhal_products.csv"
sales_data[['Category', 'Product', 'Sales Percentage']].to_csv(output_file, index=False)

print("Output saved successfully to", output_file)
