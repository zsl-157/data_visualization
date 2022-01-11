import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



#data = pd.DataFrame(columns=["name","age"],data=[["李",24],["张",10],["张",20],["宋",21]])
#data1 = pd.DataFrame(columns=["name","age"],data=[["李",29],["张",10],["张",20],["宋",21]])
#d = data['name'].apply(lambda x: '三生三世' if x=='张' else x)
#data['new'] = d
#print(data)
#p = pd.DataFrame([[]])

#dd = pd.concat([data,p],ignore_index=True)
#ddd =pd.concat([dd,data1],ignore_index=True)
#print(ddd)
#data['name'] = ['ddd','dddd','dsfdsfa','sadfdsafdsfa']
#print(data)

class Test:
    def show(self):
        print("this is Test")

class Test1(Test):
    pass

d = Test1()
d.show()
