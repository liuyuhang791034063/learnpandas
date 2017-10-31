#coding=utf-8
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

left = DataFrame({'key1':['foo','foo','bar'],
                  'key2':['one','two','one'],
                  'lval':[1,2,3]})
right = DataFrame({'key1':['foo','foo','bar','bar'],
                   'key2':['one','one','one','two'],
                   'rval':[4,5,6,7]})

left1 = DataFrame({'key':['a','b','a','a','b','c'],
                    'value':range(6)})
right1 = DataFrame({'group_val':[3.5,7]})

s1 = Series([0,1], index=['a','b'])
s2 = Series([2,3,4], index=['c','d','e'])
s3 = Series([5,6], index=['f','g'])

s4 = pd.concat([s1 * 5, s3])

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18,25,35,60,100]
group_name = ['Youth','YoungAdult','MiddleAged','Senior']
cats = pd.cut(ages, bins, labels=group_name)

np.random.seed(12345)
data = DataFrame(np.random.randn(1000,4))
print data[(np.abs(data) > 3).any(1)]


