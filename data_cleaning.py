# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 05:12:16 2022

@author: lucas
"""


import pandas as pd
#from web_scrapper import get_actualTop50CitiesSalariesDs
PATH = "C:/Users/lucas/Documents/data_science projects/data_scientist_salaries_analysis/dataset/"

def get_data_cleaned():

    # get the most actual data salaries from 50 top USA cites 
    #h1bdata_df = get_actualTop50CitiesSalariesDs()
    
    # For convinience I save as the data as csv file locally and load that bellow:
        
    glassdoor_df = pd.read_csv( PATH + 'data_cleaned_2021.csv')
    h1bdata_df = pd.read_csv(PATH + "data_scientis_salaries_on_top_50_usa_cities.csv")
    salary_ai_df = pd.read_csv(PATH + "data_science_jobs_salaries.csv", delimiter=';')
    
    
    #cleaning
    
    glassdoor_df = glassdoor_df[[ 'Job Title', 'Salary Estimate', 'Job Description', 'Rating', 'Location', 'Headquarters', 'Size', 'Founded',
           'Type of ownership', 'Sector', 'Revenue',
           'Lower Salary', 'Upper Salary',
           'Avg Salary(K)', 'company_txt', 'Job Location', 'Age', 'Python',
           'spark', 'aws', 'excel', 'sql', 'sas', 'keras', 'pytorch', 'scikit',
           'tensor', 'hadoop', 'tableau', 'bi', 'flink', 'mongo', 'google_an',
           'job_title_sim', 'seniority_by_title', 'Degree']]
    
    h1bdata_df.dropna(inplace=True)
    return (glassdoor_df, h1bdata_df, salary_ai_df)