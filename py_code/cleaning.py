# ======================================
# Customer-Transaction-Analytics PROJECT
# --------------------------------------
# Author -- Anindya Adhikari
# ======================================


# --- Import Libraries ---
import pandas as pd 
import numpy as np 



# --- Load DataSet ---
df = pd.read_csv(r"C:\Users\anind\OneDrive\Desktop\PythonVSC\Project\Customer-Transaction-Analytics\data\bank_transactions_data.csv")
print("DataSet Loaded Successfully \n")



# How many rows and columns are in the dataset, and what are the data types of each column?
'''
df.info()
print(df.shape)
'''


# Are there any duplicate transactions, and how should they be removed?
'''
df.duplicated().sum()
df_clean = df.drop_duplicates(inplace = True)
print(df.shape) 
'''


# Are there any missing values in the dataset, and which columns contain them?
'''
df.isnull().sum()
'''


# Are TransactionDate and PreviousTransactionDate in proper datetime format?
'''
print(df[['TransactionDate', 'PreviousTransactionDate']].dtypes)
'''


# What new time features can be extracted from TransactionDate such as month, day of week, and hour?