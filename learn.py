#coding=utf-8
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

data =  {'state':['ohio','Ohio','Ohio','Nevada','Nevada'],
         'year':[2000,2001,2002,2001,2002],
         'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data ,columns=['state','year','pop','debt'] ,index=['a','b','c','f','e'])
frame['debt'] = np.arange(5.)

abc = DataFrame(np.arange(12.).reshape(4,3), columns=list('bfe'),index=['Utah','Ohio','Texas','Oregon'])

de = abc.ix[2]
series2 = Series(range(3), index=['b','e','f'])
print series2
print series2 + abc