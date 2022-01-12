from pyecharts import options
from pyecharts.charts import Bar
import pandas as pd
import os
from main.exception.Base_Exception import BaseExceptionss
from main.visual.BaseD import Basedata

class BarVisual(Basedata):
    def __init__(self):
        self.data = pd.read_csv("./data.csv")
        if self.data is None:
            raise BaseExceptionss("")


    def bar(self):
        group_state = self.data.groupby(['Province_State'])['Confirmed'].sum()
        print(group_state)



d = BarVisual()
d.bar()



