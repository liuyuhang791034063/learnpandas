##coding=utf-8
from datetime import datetime
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

arr = np.random.randn(5, 5)
print arr
print arr[::2].sort(1)
print arr[:, :-1] < arr[:, 1:]