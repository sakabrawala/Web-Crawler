
import pandas as pd
import openpyxl
from pandas import DataFrame
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

class Analysis:
    
    filePath =r'C:\Users\Smit\Desktop\STQA\ApplicationData1.csv'
    df = pd.read_csv(filePath, sep='\t', thousands=',')
    
    
    df['Price'] = df['Price'].map(lambda x: x.lstrip('$'))
    res = df[df['Price'] == df['Price'].max()]
    print("Highest priced apps:- ", res)
   
    
    res1 = df[df['TotalReviews'] == df['TotalReviews'].max()]
    print("Highest reviewed app:- ", res1['Title'])
    
    df = pd.read_csv(filePath)
    sample_data_table = FF.create_table(df.head())
    
    py.iplot(sample_data_table, filename='ApplicationData1')
    
    