# data_engineering_project
Data wrangling project using Python and Pandas to clean and prepare raw sales data for analysis.
🎯 Objectives
•	Load and inspect raw sales data
•	Identify and handle:
o	Missing values
o	Duplicate records
o	Inconsistent data formats
o	Outliers
o	Categorical inconsistencies
•	Convert cleaned data into a usable format for analysis or visualization
________________________________________
🗃️ Dataset Description
The dataset contains the following fields:
Column Name	Description
order_id	Unique identifier for each order
customer_id	Unique identifier for each customer
order_date	Date when the order was placed
shipping_date	Date when the order was shipped
shipping_cost	Cost of shipping (may contain formatting issues like $)
shipping_country	Destination country (includes inconsistent casing)
shipping_city	Destination city
shipping_company	Company handling the shipment (some missing values)
________________________________________
🛠️ Tools & Libraries
•	Python
•	Pandas
•	NumPy
•	VS Code
________________________________________
🚀 Key Data Wrangling Techniques Demonstrated
•	Handling null values with pandas.isnull() and fillna()/dropna()
•	Removing duplicate rows
•	Standardizing column formats (e.g., stripping $ from cost values)
•	Converting datatypes
•	Handling categorical inconsistencies (e.g., country casing)
•	Identifying and managing outliers in numerical data
________________________________________
✅ Outcome
After completing the wrangling process, the dataset becomes clean, consistent, and ready for further analysis, visualization, or machine learning tasks.
