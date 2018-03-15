#coding:utf-8
import pandas as pd
data=pd.read_table("paper3.csv",sep=",",dtype={'fundid':str})  #fundid列识别为文本格式
a=data.sort(['todayrate'],ascending=False).head(6)[0:6]
print a

'''
n=0
try:
    for i in range(300):
        print float(data['todayrate'][i].strip('%').replace(' ','0'))
        n = n + 1
except:
    print n
'''