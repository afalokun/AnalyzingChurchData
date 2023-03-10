# -*- coding: utf-8 -*-
"""Class6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MsmiUsYWJ8d3u-MKSl1w4i1A8EWDWTgz
"""

import pandas as pd

zip_url = 'https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'

from urllib import request
request.urlretrieve(zip_url, filename='stack-overflow-developer-survey-2021.zip')


from zipfile import ZipFile
file_names = list() 
with ZipFile('stack-overflow-developer-survey-2021.zip', mode='r') as zip:
    zip.extractall()
    for file in zip.infolist():
        file_names.append(file.filename)
        print(file.filename)

#read first csv into dataframe
srp = pd.read_csv('survey_results_public.csv')
srp.head()

srp.info()

import seaborn as sns

#cell 6
a = sns.scatterplot(data=polls, x='adjpoll_clinton', y='adjpoll_trump')