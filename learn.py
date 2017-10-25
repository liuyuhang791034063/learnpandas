#coding=utf-8
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

data =  {'state':['ohio','Ohio','Ohio','Nevada','Nevada'],
         'year':[2000,2001,2002,2001,2002],
         'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame({'b':[4,-3,np.nan,8], 'a':[10,-90,20,30]})

abc = DataFrame(np.arange(12).reshape(4,3), columns=list('bfe'),index=['One','Two','There','Four'])

de = abc.ix[2]
series = Series([5,32,23,56], index=['b','a','e','f'])

print frame
print frame.describe()ttt
