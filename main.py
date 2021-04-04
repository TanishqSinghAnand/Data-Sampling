from numpy.lib.function_base import average
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import csv
import statistics
df = pd.read_csv('data.csv')
populationData = df["reading_time"].tolist()

mean = statistics.mean(populationData)
std = statistics.stdev(populationData)
print("Mean = ", mean)
print("Standard Deviation : ", std)

def randomMean(counter):
    times = 100
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(populationData)-1)
        value = populationData[randomIndex]
        dataset.append(value)
    mean_dataset = statistics.mean(dataset)
    std_dataset = statistics.stdev(dataset)
    # print("Mean of 2nd data : " , mean_dataset)
    # print("Stdev of 2nd data : " , std_dataset)
    return mean_dataset


def show_fig(mean_list):
    df = mean_list
    meanOfSamplingDistribution = statistics.mean(mean_list)
    print(meanOfSamplingDistribution)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    # fig.add_trace(go.Scatter(x=[mean , mean],y=[0,1],mode = "lines" , name = "MEAN"))
    fig.show()



def setup():
    mean_list = []
    for i in range(0,100):
        setOfMeans = randomMean(30)
        mean_list.append(setOfMeans)
    show_fig(mean_list)

setup()
