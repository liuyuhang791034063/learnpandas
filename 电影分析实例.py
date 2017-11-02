#coding=utf-8
from pandas import Series,DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')
s = movie_pd[:5][['title','vote_count','score']]
title = list(s['title'])
score = list(s['score'])
vote_count = list(s['vote_count'])
dict = {'title':title,
        'score':score,
        'vote_count':vote_count}
s = DataFrame(dict,index=title)
s.plot(subplots= True, sharex= True)
plt.show()