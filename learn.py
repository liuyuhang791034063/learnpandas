#coding=utf-8
from pandas import DataFrame
import pandas as pd
import numpy as np

data =  {'state':['ohio','Ohio','Ohio','Nevada','Nevada'],
         'year':[2000,2001,2002,2001,2002],
         'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data , columns=['state','year','pop','debt'])
frame['debt'] = np.arange(5.)
print frame
del frame['debt']
print frame