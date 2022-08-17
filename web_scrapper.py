"""
Credits for basecode


"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import pickle
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def get_dataWithExeceptionHandler(whole_data, index):
    tmp_lst=[]
    for i in whole_data:
            try:
                tmp_lst.append(i[index])
            except IndexError:
                tmp_lst.append("null")
    return tmp_lst
def get_actualTop50CitiesSalariesDs():
    TOP_50_USA_CITIES = ["NEW+YORK","LOS+ANGELES","CHICAGO","HOUSTON","PHILADELPHIA","PHOENIX","SAN+ANTONIO","SAN+DIEGO","DALLAS","SAN+JOSE","AUSTIN","JACKSONVILLE","SAN+FRANCISCO","INDIANAPOLIS","COLUMBUS","FORT+WORTH","CHARLOTTE","SEATTLE","DENVER","EL+PASO","DETROIT","WASHINGTON","BOSTON","MEMPHIS","NASHVILLE","PORTLAND+ORE.","OKLAHOMA+CITY","LAS+VEGAS","BALTIMORE","LOUISVILLE","MILWAUKEE","ALBUQUERQUE","TUCSON","FRESNO","SACRAMENTO","KANSAS+CITY+MO.","LONG+BEACH","MESA","ATLANTA","COLORADO+SPRINGS","VIRGINIA+BEACH","RALEIGH","OMAHA","MIAMI","OAKLAND","MINNEAPOLIS","TULSA","WICHITA","NEW+ORLEANS","ARLINGTON+TEXAS"]
    links = ['https://h1bdata.info/index.php?em=&job=Data+Scientist&city=' + city+ '&year=All+Years' for city in TOP_50_USA_CITIES]
    
    # Scrape table data from each of the above links and store in a list
    jobs_list = []
    for link in links:
        page_link = link
        page_response = requests.get(page_link, timeout=1000)
        page_content = BeautifulSoup(page_response.content, 'lxml')
    
        for row in page_content.find_all('tr')[1:]:
            row_data = []
            for i in row:
                row_data.append(i.text)
            jobs_list.append(row_data)
    # Put everything into dataframes for easier processing
    ds_jobs_df = pd.DataFrame()
    ds_jobs_df['company'] = [i[0] for i in jobs_list]
    
    
    
    
    ds_jobs_df['title'] = get_dataWithExeceptionHandler(jobs_list,1)
    
    ds_jobs_df['salary'] = get_dataWithExeceptionHandler(jobs_list,2)
    #ds_jobs_df['salary'] = ds_jobs_df['salary'].astype(float)
    
    ds_jobs_df['location'] = get_dataWithExeceptionHandler(jobs_list,3)
    
    ds_jobs_df['date'] =get_dataWithExeceptionHandler(jobs_list,4)
    ds_jobs_df['date'] =  ds_jobs_df['date'] 
    
    return ds_jobs_df