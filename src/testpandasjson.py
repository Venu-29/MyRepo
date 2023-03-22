import pandas as pd
# load a csv file
e_commerce_data_path_csv = "C:\\Users\\venuy\\Mylearning\\MyRepo\\data\\data.csv"
e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)
print(e_commerce_csv_df)
print(e_commerce_csv_df.columns)
print(e_commerce_csv_df.dtypes)
# load a json file
e_commerce_data_path_json = "C:\\Users\\venuy\\Mylearning\\MyRepo\\data\\data_subset.json"
e_commerce_json_df = pd.read_json(
    e_commerce_data_path_json,  encoding='unicode_escape')
print(e_commerce_json_df)
print(e_commerce_json_df.columns)
print(e_commerce_json_df.dtypes)

# join the csv and the json to a new dataframe
print(len(e_commerce_csv_df) + len(e_commerce_json_df))
# > 1004
e_commerce_appended_df=e_commerce_csv_df.append(e_commerce_json_df)

print(len(e_commerce_appended_df))

print(e_commerce_appended_df.head(10))
##########################################################
# Merging of dataframes
##########################################################

my_json = '{"Country" : ["United Kingdom", "France", "Australia", "Netherlands"], "Language":["English" , "French", "English" , "Dutch"]}'
json_df = pd.read_json(my_json)
print(json_df)

e_commerce_csv_df = e_commerce_csv_df.merge(json_df,on = "Country")
print(e_commerce_csv_df)


# do a lambda to change of the timestamp from / to epoch
# before
print(e_commerce_appended_df.dtypes)
e_commerce_appended_df['InvoieDate']= pd.to_datetime(
    e_commerce_appended_df['InvoiceDate'])
print(e_commerce_appended_df.dtypes)

# Filter out two columns "Country" and "Quantity"
print(e_commerce_appended_df.columns)
# > Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# >        'UnitPrice', 'CustomerID', 'Country'],
# >       dtype='object')

e_commerce_appended_df = e_commerce_appended_df.drop(
    ["Country", "Quantity"], axis="columns")
print(e_commerce_appended_df.columns)
# > Index(['InvoiceNo', 'StockCode', 'Description', 'InvoiceDate', 'UnitPrice',
# >        'CustomerID'],
# >       dtype='object')

# normalize the dataframe
# normalize a Pandas Column with Maximum Absolute Scaling using Pandas
'''
e_commerce_csv_df.head(5)
# >   InvoiceNo StockCode                          Description  Quantity     InvoiceDate  UnitPrice  CustomerID         Country
# > 0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  12/1/2010 8:26       2.55       17850  United Kingdom
# > 1    536365     71053                  WHITE METAL LANTERN         6  12/1/2010 8:26       3.39       17850  United Kingdom
# > 2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8  12/1/2010 8:26       2.75       17850  United Kingdom
# > 3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6  12/1/2010 8:26       3.39       17850  United Kingdom
# > 4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6  12/1/2010 8:26       3.39       17850  United Kingdom

cols_to_normalize = ["Quantity", "UnitPrice"]


def absolute_maximum_scale(series):
    return series / series.abs().max()

for column in cols_to_normalize:
    e_commerce_csv_df[column] = absolute_maximum_scale(
            e_commerce_csv_df[column])


e_commerce_csv_df.head(5)
# >   InvoiceNo StockCode                          Description  Quantity     InvoiceDate  UnitPrice  CustomerID         Country
# > 0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER      0.01  12/1/2010 8:26   0.015455       17850  United Kingdom
# > 1    536365     71053                  WHITE METAL LANTERN      0.01  12/1/2010 8:26   0.020545       17850  United Kingdom
# > 2    536365    84406B       CREAM CUPID HEARTS COAT HANGER  0.013333  12/1/2010 8:26   0.016667       17850  United Kingdom
# > 3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE      0.01  12/1/2010 8:26   0.020545       17850  United Kingdom
# > 4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.      0.01  12/1/2010 8:26   0.020545       17850  United Kingdom

# pivot the normalized dataframe

e_commerce_csv_df["Country"].unique()
# > <StringArray>
# > ['United Kingdom', 'France', 'Australia', 'Netherlands']
# > Length: 4, dtype: string

e_commerce_csv_df["unique_id"] = e_commerce_csv_df["InvoiceNo"] + \
    e_commerce_csv_df["StockCode"] + \
    e_commerce_csv_df["CustomerID"].astype("str")

e_commerce_pivoted = (e_commerce_csv_df
                      .filter(items=["unique_id", "UnitPrice", "Country"])
                      .pivot_table(
                          index="unique_id",
                          columns="Country",  # Column(s) we want to pivot.
                          # Column with values that we want to have in our new pivoted columns.
                          values="UnitPrice",
                          # Even if there is not aggregation we need to provide aggregation funciton.
                          aggfunc="mean"
                      )
                      .reset_index()
                      )
e_commerce_pivoted
# > Country          unique_id  Australia  France  Netherlands  United Kingdom
# > 0         5363652173017850       <NA>    <NA>         <NA>        0.025758
# > 1         5363652275217850       <NA>    <NA>         <NA>        0.046364
# > 2         5363657105317850       <NA>    <NA>         <NA>        0.020545
# > 3        53636584029E17850       <NA>    <NA>         <NA>        0.020545
# > 4        53636584029G17850       <NA>    <NA>         <NA>        0.020545
# > ..                     ...        ...     ...          ...             ...
# > 940      C5363912198417548       <NA>    <NA>         <NA>        0.001758
# > 941      C5363912255317548       <NA>    <NA>         <NA>            0.01
# > 942      C5363912255617548       <NA>    <NA>         <NA>            0.01
# > 943      C5363912255717548       <NA>    <NA>         <NA>            0.01
# > 944      C5365062296017897       <NA>    <NA>         <NA>        0.025758
# >
# > [945 rows x 5 columns]

# store dataframe as parquet file
e_commerce_pivoted.to_parquet('./data/e_commerce_pivoted.parquet.gzip',
                              compression='gzip')
# > None

# read parquet file

pd.read_parquet(
    './data/e_commerce_pivoted.parquet.gzip')
# > Country          unique_id  Australia  France  Netherlands  United Kingdom
# > 0         5363652173017850       <NA>    <NA>         <NA>        0.025758
# > 1         5363652275217850       <NA>    <NA>         <NA>        0.046364
# > 2         5363657105317850       <NA>    <NA>         <NA>        0.020545
# > 3        53636584029E17850       <NA>    <NA>         <NA>        0.020545
# > 4        53636584029G17850       <NA>    <NA>         <NA>        0.020545
# > ..                     ...        ...     ...          ...             ...
# > 940      C5363912198417548       <NA>    <NA>         <NA>        0.001758
# > 941      C5363912255317548       <NA>    <NA>         <NA>            0.01
# > 942      C5363912255617548       <NA>    <NA>         <NA>            0.01
# > 943      C5363912255717548       <NA>    <NA>         <NA>            0.01
# > 944      C5365062296017897       <NA>    <NA>         <NA>        0.025758
# >
# > [945 rows x 5 columns]
'''