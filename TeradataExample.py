# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:23:26 2018

@author: KBULMER
"""

import pandas as pd
import teradata as td
import password as pw
import seaborn as sb
import matplotlib.pyplot as plt

udaExec = td.UdaExec(appName="Source",version="1.0",logConsole=False)
conn_s = udaExec.connect(method="odbc",dsn="CLAIM_TERADATA_DEV",username=pw.username,password=pw.password)

print("Connection established")

data = pd.read_sql("SELECT * FROM DBC.BAR_MapsV", conn_s)
NumRows = pd.read_sql("SELECT COUNT (*) FROM DBC.BAR_MAPSV", conn_s)
#data = pd.read_sql("SELECT  FROM DBC.BAR_StatsV", conn_s)
dataframe1 = pd.DataFrame(data)
dataframe1.to_csv('MapNameTeradata.csv',header=True, sep=',', index=False,)
print("MapNameTeradata.csv has been created")

print('Graph has been created')
f, ax = plt.subplots(figsize=(12,4))
vis1 = sb.barplot(x='MapName',y='MapSlot',data=dataframe1, palette='rocket')
for p in vis1.patches:
    height = int(p.get_height())
    vis1.text(p.get_x()+p.get_width()/2,
            height+.05, int(height), ha="center",color='black') 
ax.set(ylim=(0, 3.0), xlabel="Map Name")

data2 = pd.read_sql("SELECT * FROM DBC.ViewStatsV",conn_s)
df = pd.DataFrame(data2)
df.to_csv("StatsDataTera.csv",header=True, sep=',',index=False)
