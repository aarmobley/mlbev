# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:22:53 2023

@author: Aaron Mobley
"""

#MLB dataset 
#import data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
import  statsmodels.api as sm
from scipy.stats import boxcox

mlb = pd.read_csv(r'C:\Users\Aaron Mobley\Desktop\R and Pythin data\mlbexitvelo.csv')

#Explore data
mlb.head()
mlb.columns.tolist()
mlb.describe()
mlb.info()
mlb.isna().any()
mlb['year'].info

#drop na values from average_homerun

mlb.dropna(inplace=True)
mlb.isna().any()

#Find the top 10 players in exit velocity each year from 2015 to 2022

TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2015]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2015 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2015)


# Loop through every year from 2015-2022 to find top 10
TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2016]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2016 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2016)
    
TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2017]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2017 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2017)
    
TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2018]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2018 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2018)
    
TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2019]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2019 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2019)
    
TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2020]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2020 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2020)

TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2021]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2021 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2021)
    
TopEV = 'average_ev'
for year in range(2015, 2022):
    yearEV = mlb[mlb['year'] == 2022]
    
    yearEV_sorted = yearEV.sort_values(by=TopEV, ascending=False)
    
    top2022 = yearEV_sorted.head(10)
    
    print(f'Top 10 players in {TopEV} for {year}:')
    print(top2022)
    
    
#combine dataframes for each year
TOP_10 = pd.concat([top2015, top2016, top2017, top2018, top2019, top2020, top2021, top2022],
                   ignore_index=True)

# Print the result
print(TOP_10)
FINALMLB = TOP_10

#export to csv file
FINALMLB.to_csv(r'C:\Users\Aaron Mobley\Desktop\Python\FINALMLB.csv')



## Create correlation matrix - drop categorical variables

mlbcorr = mlb.drop(['id', 'rank', 'year', 'player', 'barrels_plate_appearance_percentage'], 
                   axis = 1)
mlbcorr.head()

mlb1 = mlbcorr.corr(method = 'pearson')

#correlation matrix for only max ev and batted ball events
corr_matrix = mlbcorr[["max_ev", "batted_ball_events"]].corr(method="pearson")
#there is a decent amount of positive correlation 

#high positive correlation with line drives/flyballs and average exit velocity


