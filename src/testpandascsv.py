import pandas as pd
# load a csv file
e_commerce_data_path_csv = "C:\\Users\\venuy\\Mylearning\\MyRepo\\data\\data.csv"
e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)
print(e_commerce_csv_df)
print(e_commerce_csv_df.columns)
print(e_commerce_csv_df.dtypes)
# show columns
'''
e_commerce_csv_df.columns
# > Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# >        'UnitPrice', 'CustomerID', 'Country'],
# >       dtype='object')

# show types
e_commerce_csv_df.dtypes
# > InvoiceNo       object
# > StockCode       object
# > Description     object
# > Quantity         int64
# > InvoiceDate     object
# > UnitPrice      float64
# > CustomerID     float64
# > Country         object
# > dtype: object

# change types
e_commerce_csv_df = e_commerce_csv_df.convert_dtypes()
# New dtypes
e_commerce_csv_df.dtypes
# > InvoiceNo       string
# > StockCode       string
# > Description     string
# > Quantity         Int64
# > InvoiceDate     string
# > UnitPrice      Float64
# > CustomerID       Int64
# > Country         string
# > dtype: object

# Cast a pandas object to a specified dtype dtype via dictionary, quantity from int64 to float64, and customerID from int64 to flat64. This
# is just a dummy example, and I am not telling you that converting customerid to float is a smart move:)

temp_dtype_change_df = e_commerce_csv_df.astype(
    {'Quantity': 'float64',
     'CustomerID': 'float64'
     }
)
temp_dtype_change_df.dtypes
# > InvoiceNo       string
# > StockCode       string
# > Description     string
# > Quantity       float64
# > InvoiceDate     string
# > UnitPrice      Float64
# > CustomerID     float64
# > Country         string
# > dtype: object

# load json
'''