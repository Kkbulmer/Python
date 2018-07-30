# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:03:09 2018

@author: KBULMER
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


df = pd.read_csv('Week1.csv')
nflData = pd.DataFrame(df)


#Makes the team column the select index
# UniqueIndex = nflData.set_index("Team", drop = False)
# print(UniqueIndex.head())

AFC = df['Conference'] == 'AFC' 

sb.set(style="whitegrid")
print('Graph created')

#graph1
sb.set_color_codes('pastel')
f, ax = plt.subplots(figsize=(8,10))
vis2 = sb.barplot(x='PointsScored',y='Team',data=df, palette='rocket')
vis2.set_title('Points Scored by Team', fontsize='xx-large')

#ADDING HUE WILL ONLY LABEL THE ONES WHO FALL UNDER THE FIRST VALUE OF HUE
for p in vis2.patches: #for number of columns in vis4 graph
    width = int(p.get_width()) #gets integer value of widths for each bar
    vis2.text(.5+p.get_width(), (p.get_y()+0.55*p.get_height()),int(width),\
             va='center',color='black') 
plt.show()

#graph2
df[df.Conference=='AFC'].plot.barh(x='Team',y='TotalYards',figsize=(8,10),\
  title="Total Yards by Team",legend=False, fontsize='medium')


#graph3
f, ax = plt.subplots(figsize=(10, 10))
vis4 = sb.barplot(x='TotalYards',y='Team', data=df, color='b',\
                  label='Total Yards')
vis4 = sb.barplot(x='RushingYards', y='Team', data=df, color='g',\
                  label='Rushing Yards')
vis4.set_title('Rushing Yards out of Total Yards per Team', fontsize='xx-large')
ax.legend(ncol=2, loc="lower right", frameon=True)
for p in vis4.patches: #for number of columns in vis4 graph
    width = int(p.get_width()) #gets integer value of widths for each bar
    vis4.text(5+p.get_width(), (p.get_y()+0.55*p.get_height()),int(width),\
             va='center',color='black') 
ax.set(xlim=(0, 600), ylabel="", xlabel="Yards")


#graph4
vis3 = sb.lmplot(y='TotalTD', x='TotalYards', data=df,fit_reg=False,\
                 hue='Division', col='Conference',palette="rocket",\
                 size=5, aspect=1.25)





