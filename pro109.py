import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
import pandas as pd

d = pd.read_csv("StudentsPerformance.csv")
result1 = d["reading score"].tolist()

mean = sum(result1)/len(result1)
mode = statistics.mode(result1)
median = statistics.median(result1)
stdeviation = statistics.stdev(result1)

print(mean)
print(mode)
print(median)
print(stdeviation)

firstsdstart,firstsdend = mean - stdeviation,mean + stdeviation
secondsdstart,secondsdend = mean - (2*stdeviation),mean + (2*stdeviation)
thirdsdstart,thirdsdend = mean - (3*stdeviation),mean + (3*stdeviation)
fig = ff.create_distplot([result1],["result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean")) 
fig.add_trace(go.Scatter(x = [firstsdstart,firstsdstart],y = [0,0.17],mode = "lines",name = "sd1"))
fig.add_trace(go.Scatter(x = [firstsdend,firstsdend],y = [0,0.17],mode = "lines",name = "sd1"))
fig.add_trace(go.Scatter(x = [secondsdstart,secondsdstart],y = [0,0.17],mode = "lines",name = "sd2"))
fig.add_trace(go.Scatter(x = [secondsdend,secondsdend],y = [0,0.17],mode = "lines",name = "sd2"))

fig.show()
listofdatawithinsd1 = [result for result in result1 if result > firstsdstart and result < firstsdend]
print("{}% of data lies within 1 standard deviation".format(len(listofdatawithinsd1)*100/len(result1)))
listofdatawithinsd2 = [result for result in result1 if result > secondsdstart and result < secondsdend]
print("{}% of data lies within 2 standard deviation".format(len(listofdatawithinsd2)*100/len(result1)))
listofdatawithinsd3 = [result for result in result1 if result > thirdsdstart and result < thirdsdend]
print("{}% of data lies within 3 standard deviation".format(len(listofdatawithinsd3)*100/len(result1)))