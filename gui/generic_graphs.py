import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class Graphs:
    def __init__(self, csv_file_path, graph_name):
        self.csv_file_path = csv_file_path
        self.graph_name = graph_name 

def frequency_per_section(graphs_object, word_frequency): # variable word_frequency is the word that you want to be graphed by its frequency
    data = pd.read_csv(graphs_object.csv_file_path)
    data.dropna(inplace = True)
    data = data[data["Word"].isin(word_frequency)]
    data.plot.bar(x = 'Section_ID', y = 'Frequency', rot = 0)
    plt.suptitle(graphs_object.graph_name)
    plt.show()

def frequency_comparison(graphs_object, important_word_list):
    data = pd.read_csv(graphs_object.csv_file_path)
    data.dropna(inplace = True)
    data = data[data["Word"].isin(important_word_list)]
    data.plot(kind='line',x='Word',y='Frequency')
    plt.suptitle(graphs_object.graph_name)
    plt.show()

def word_count_section(graphs_object):
    data = pd.read_csv(graphs_object.csv_file_path)
    dx = data.plot(x='Section_Index',y='Total_Word_Count')
    dx.set_xlim(1,data['Section_Index'].max())
    plt.suptitle(graphs_object.graph_name)
    plt.show()

def multi_word_frequency_alternative(graphs_object, important_word_list):
    data = pd.read_csv(graphs_object.csv_file_path)
    data.dropna(inplace = True)
    data = data[data["Word"].isin(important_word_list)]
    data = data.set_index(['Section_ID','Word']).Frequency
    data.unstack().plot(kind='bar')
    plt.suptitle(graphs_object.graph_name)
    plt.show()

def multi_word_frequency(graphs_object, important_word_list):
    data = pd.read_csv(graphs_object.csv_file_path)
    data.dropna(inplace = True)
    data = data[data["Word"].isin(important_word_list)]
    test = dict(tuple(data.groupby('Word')))
    frame1 = pd.DataFrame(test[important_word_list[0]], columns = ['Section_ID', 'Frequency'])
    frame2 = pd.DataFrame(test[important_word_list[1]], columns = ['Section_ID', 'Frequency'])
    xmax = frame1['Section_ID'].max() if frame1['Section_ID'].max() > frame2['Section_ID'].max() else frame2['Section_ID'].max()
    ax = frame1.plot(x='Section_ID',y='Frequency')
    bx = frame2.plot(x='Section_ID',y='Frequency',ax=ax)
    bx.legend([important_word_list[0],important_word_list[1]])
    bx.set_xlim(1,xmax)
    plt.suptitle(graphs_object.graph_name)
    plt.show()