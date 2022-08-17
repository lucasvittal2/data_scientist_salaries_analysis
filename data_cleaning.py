# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 05:12:16 2022

@author: lucas
"""


import pandas as pd
from web_scrapper import get_actualTop50CitiesSalariesDs

PATH = "C:/Users/lucas/Documents/data_science projects/data_scientis_sallary_analysis/dataset/"
glassdoor_df = pd.read_csv( PATH + 'data_cleaned_2021.csv')
# get the most actual data salaries from 50 top USA cites 
#h1bdata_df = get_actualTop50CitiesSalariesDs()

# For convinience a save the data locally and load that bellow:

h1bdata_df = pd.read_csv(PATH + "data_scientis_salaries_on_top_50_usa_cities.csv")