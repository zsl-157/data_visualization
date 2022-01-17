from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd
import numpy as np
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
        group_state = group_state.reset_index(name="sum")
        x = [x for x in group_state['Province_State']]
        y = [y for y in group_state['sum']]
        Bar(init_opts=opts.InitOpts(width="1500px")).add_xaxis(x).add_yaxis("确诊人数",y)\
            .set_global_opts(opts.TitleOpts(title="2021美国疫情各洲确诊人数柱状图",pos_left="700px"),
                             opts.LegendOpts(pos_left='right'),opts.AxisOpts(name="Province_State",axistick_opts={"rotate":90}))\
            .set_series_opts(opts.LabelOpts(font_size=10,color="red"))\
            .set_colors("#3cb034").render("Conv21-American.html")



d = BarVisual()
d.bar()



