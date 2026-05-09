import numpy as np
import pandas as pd

# Завдання 1


# df_a = pd.DataFrame({
#     'EmployeeID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Department': ['HR', 'Engineering', 'Marketing']
# })

# df_b = pd.DataFrame({
#     'EmployeeID': [4, 5],
#     'Name': ['David', 'Eva'],
#     'Department': ['Finance', 'IT']
# })
# df = pd.concat([df_a, df_b], ignore_index=True)
# print(df)

# # Завдання 2

# orders_df = pd.DataFrame({
#     'OrderID': [1001, 1002, 1003, 1004],
#     'CustomerID': [1, 2, 1, 3],
#     'ProductID': [501, 502, 503, 504],
#     'Quantity': [2, 1, 5, 3]
# })

# customers_df = pd.DataFrame({
#     'CustomerID': [1, 2, 3, 4],
#     'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
# })

# m_df = pd.merge(orders_df, customers_df, on=['CustomerID', 'ProductID'], how='inner', indicator=True)
# print(m_df)

# # Завдання 3



# np.random.seed(0)
# transactions_df = pd.DataFrame({
#     'TransactionID': range(1, 100001),
#     'UserID': np.random.randint(1, 1001, size=100000),
#     'ProductID': np.random.randint(1, 500, size=100000),
#     'Date': pd.date_range(start='2023-01-01', periods=100000, freq='T'),
#     'Amount': np.random.uniform(10.0, 1000.0, size=100000)
# })

# products_df = pd.DataFrame({
#     'ProductID': range(1, 500),
#     'ProductName': [f'Product_{i}' for i in range(1, 500)]
# })
# transactions_df['Amount'] = transactions_df['Amount'].astype('float32')

# optimized_df = transactions_df.set_index(['UserID', 'ProductID'])
# print(optimized_df.info())
# # Завдання 4



# df_sales = pd.DataFrame({
#     'SaleID': [2001, 2002, 2003, 2004, 2005],
#     'StoreID': [10, 20, 10, 30, 20],
#     'ProductID': [301, 302, 303, 301, 304],
#     'UnitsSold': [50, 60, 70, 80, 90]
# })

# df_suppliers = pd.DataFrame({
#     'SupplierID': [401, 402, 403, 404],
#     'ProductID': [301, 302, 303, 305],
#     'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
# })
# sales_optimized = df_sales.set_index(['StoreID', 'ProductID'])
# print(sales_optimized)