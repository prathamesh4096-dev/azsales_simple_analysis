# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:35:45 2026

@author: Prathamesh
"""

#%%                                                                             #Data Loading and column analysis
import pandas as pd
import matplotlib.pyplot as plt
azsdata = pd.read_csv('amazon_sales_report.csv')                                  #Load csv into dataframe 'azsdata'
df = azsdata.head(5)

azsdata.info()                                                                    #Check the dimensions and contents of the dataframe
azsdata.shape
azsdata.columns
azsdata.dtypes

#%%              Modifying the table by removing columns and records that provide no benefit to our analysis


azsdata.columns = azsdata.columns.str.strip()                                             #Trimming column names
drop_cols = [
    'Unnamed: 22',
    'Style',
    'SKU',
    'ASIN',
    'ship-postal-code',
    'fulfilled-by',
    'ship-country',
    'currency',
    'index',
    'promotion-ids',
    'ship-city'
]
                                                                                        #Data Cleaning
azsdata = azsdata.drop(columns = drop_cols)                                             #Drop unnecessary columns

azsdata.drop_duplicates(inplace = True)                                                 #Drop duplicates
                                                                                                         
azsdata.dropna(inplace = True)                                                       #Drop null values                            

df_sample = azsdata.head(10)
#%%    Cleaning State Names
# Normalize all state names first
azsdata['ship-state'] = (
    azsdata['ship-state']
    .astype(str)
    .str.strip()
    .str.upper()
)

# Incorrect -> correct mappings
state_corrections = {

    'RAJSHTHAN': 'RAJASTHAN',
    'RAJSTHAN': 'RAJASTHAN',
    'RJ': 'RAJASTHAN',

    'ORISSA': 'ODISHA',

    'NEW DELHI': 'DELHI',

    'PONDICHERRY': 'PUDUCHERRY',

    'PB': 'PUNJAB',

    'AR': 'ARUNACHAL PRADESH',

    'NL': 'NAGALAND',

    'PUNJAB/MOHALI/ZIRAKPUR': 'PUNJAB',

    'ANDAMAN & NICOBAR ': 'ANDAMAN & NICOBAR',

    'DADRA AND NAGAR': 'DADRA AND NAGAR HAVELI'
}

# Replace incorrect values
azsdata['ship-state'] = azsdata['ship-state'].replace(state_corrections)

# View cleaned unique states
states = sorted(azsdata['ship-state'].unique())

#Cleaning Category Names
azsdata['Category'] = (
    azsdata['Category']
    .astype(str)
    .str.strip()
    .str.upper()
)


#%%
azsdata.to_csv('Amazon_Sales_Report_Cleaned.csv')                               #Save cleaned data as csv in case it is needed for a different project

#%%

#Sales per state

state_sales = azsdata.groupby('ship-state')['Amount'].sum().sort_values(ascending = False)

state_sales.plot(kind = 'bar')
plt.xlabel('State')
plt.ylabel('Sales')
plt.show()

#%%

#Quantity by category


cat_sales = azsdata.groupby('Category')['Qty'].sum().sort_values()

plt.figure(figsize=(8,8))

plt.pie(
    cat_sales,
    labels=None,
    autopct='%1.1f%%'
)

plt.legend(                             #Labels
    cat_sales.index,
    title='Category',
    loc='center left',
    bbox_to_anchor=(1, 1)
)

plt.title('Quantity by Category')

plt.show()