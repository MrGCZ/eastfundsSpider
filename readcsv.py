#coding:utf-8
import pandas as pd
data=pd.read_table("paper.csv",sep=",",dtype={'fundid':str})  #fundid列识别为文本格式
#a=data.sort(['todayrate'],ascending=True).head(15)[0:15]

#绩优基金低谷策略
qu75week=data['weekrate'].quantile(0.75)
qu75threemonth=data['threemonthrate'].quantile(0.75)
qu75sixmonth=data['sixmonthrate'].quantile(0.75)
qu75yearrate=data['yearrate'].quantile(0.75)
qu10todayrate=data['todayrate'].quantile(0.10)
qu5todayrate=data['todayrate'].quantile(0.05)
print qu75threemonth,qu75sixmonth,qu75yearrate,qu10todayrate
a=data[(data['todayrate']<qu5todayrate)&(data['weekrate']>qu75week)&(data['threemonthrate']>qu75threemonth)&(data['sixmonthrate']>qu75sixmonth)&(data['yearrate']>qu75yearrate)]
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