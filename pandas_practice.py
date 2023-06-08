import numpy as np
import pandas as pd

Bank_df_1 = pd.DataFrame({'Bank_Client_Id': [1, 2, 3, 4, 5],
                          'First': ['Tony', 'Bobby', 'Alex', 'John', 'Jim'],
                          'Last': ['Robbins', 'Maxine', 'Georgina', 'Troopa', 'Bin']})
Bank_df_2 = pd.DataFrame({'Bank_Client_Id': [6, 7, 8, 9, 10],
                          'First': ['Lonny', 'Nikola', 'Kobe', 'Michael', 'Stan'],
                          'Last': ['Walker', 'Jokic', 'Bryant', 'Jordan', 'Van Gundy']})

# Obtained new information (salary) about bank customers
annual_salary_df = pd.DataFrame({'Bank_Client_Id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'Annual Salary': [20000, 30000, 50000, 20000, 10000, 1200000, 1500000, 
                                                   40000000, 50000000, 10000000]})
annual_salary_df

# Concatenate both bank_df_1 and bank_df_2
Bank_df_concat = pd.concat([Bank_df_1, Bank_df_2])
Bank_df_concat

# Merging client names
Bank_df_all = pd.merge(Bank_df_concat, annual_salary_df, on = 'Bank_Client_Id', how = 'inner')
Bank_df_all


# I became a new client to the bank
new_client = pd.DataFrame({'Bank_Client_Id': [11],
                           'First': ['Augustine'],
                           'Last': ['Lee'],
                           'Annual Salary': [150000]})
new_client
# Add this new dataframe to the original dataframe 'bank_df_all'
Bank_df_all = pd.concat([Bank_df_all, new_client])
Bank_df_all

# Combining the first + last columns into a new column labeled Full name
Bank_df_all['Full Name'] = Bank_df_all['First'] + ' ' + Bank_df_all['Last']
Bank_df_all = Bank_df_all[['Bank_Client_Id', 'First', 'Last', 'Full Name', 'Annual Salary']]
Bank_df_all
