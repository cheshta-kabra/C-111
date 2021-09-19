import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random 
import csv
import pandas as pd 

df=pd.read_csv('medium_data.csv')
data=df['claps'].tolist()

mean_pop=statistics.mean(data)
std_dev_pop=statistics.stdev(data)
print (mean_pop)
print (std_dev_pop)


FStd_devStart,FStd_DevEnd=mean_pop-std_dev_pop,mean_pop+std_dev_pop
SStd_devStart,SStd_DevEnd=mean_pop-(std_dev_pop*2),mean_pop+(std_dev_pop*2)
TStd_devStart,TStd_DevEnd=mean_pop-(std_dev_pop*3),mean_pop+(std_dev_pop*3)
fig=ff.create_distplot([data],['claps'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_pop,mean_pop],y=[0,0.17],mode='lines',name='mean_pop'))
fig.add_trace(go.Scatter(x=[FStd_devStart,FStd_devStart],y=[0,0.17],mode='lines',name='Std_dev1'))
fig.add_trace(go.Scatter(x=[FStd_DevEnd,FStd_DevEnd],y=[0,0.17],mode='lines',name='Std_dev1'))
fig.add_trace(go.Scatter(x=[SStd_devStart,SStd_devStart],y=[0,0.17],mode='lines',name='Std_dev2'))
fig.add_trace(go.Scatter(x=[SStd_DevEnd,SStd_DevEnd],y=[0,0.17],mode='lines',name='Std_dev2'))
fig.show()
zscore=(64.908-mean_pop)/std_dev_pop
print (zscore)