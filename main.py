import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=sum(data)/len(data)
sd=statistics.stdev(data)

print("mean is -->",mean)
print("standard deviation is -->",sd)

first_sd_start,first_sd_end=mean,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

list_of_data_within_1_sd=[result for result in data if result>first_sd_start and result < first_sd_end]
list_of_data_within_2_sd=[result for result in data if result>second_sd_start and result < second_sd_end]
list_of_data_within_3_sd=[result for result in data if result>third_sd_start and result < third_sd_end]

print("{}% of data for height lies within 1 standard deviation".format(len(list_of_data_within_1_sd)*100.0/len(data)))
print("{}% of data for height lies within 2 standard deviation".format(len(list_of_data_within_2_sd)*100.0/len(data)))
print("{}% of data for height lies within 3 standard deviation".format(len(list_of_data_within_3_sd)*100.0/len(data)))

fig=ff.create_distplot([data],["reading scores"],show_hist=False)
fig.show()
