#coding=utf-8
from pandas import DateFrame
import pandas as pd

data =  {'state':['ohio','Ohio','Ohio','Nevada','Nevada'],
         'year':[2000,2001,2002,2001,2002],
         'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DateFrame(data)
print frame