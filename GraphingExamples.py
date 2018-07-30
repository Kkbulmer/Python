# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:49:00 2018

@author: KBULMER
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loads a pre-loaded dataframe caleld tips.
df = sns.load_dataset("tips")
#groups the values containing a day into 1 and counts the amount of that day there are.
groupedvalues=df.groupby('day').sum().reset_index()

#creates a palette based off of length of days in the variable
pal = sns.color_palette("Greens_d", len(groupedvalues))\
#sorts the values by the total bill
rank = groupedvalues["total_bill"].argsort().argsort() 
#create a bargraph with the days at the x, tip price as the y, using the grouped data we created.
g=sns.barplot(x='day',y='tip',data=groupedvalues, palette=np.array(pal[::-1])[rank])

#labels the prices for each bar plot
for index, row in groupedvalues.iterrows():
    g.text(row.name,row.tip, round(row.total_bill,2), color='black', ha="center")


plt.show()

print(df.head())
