import matplotlib.pyplot as plt
import numpy as np

import basic_functions as bf

def graph_frequency_histogram(arr):
    """
    This function generates a graph of the frequencies of the elements in the input array, arr
    This function utilizes matplotlib and will produce errors if the package is not installed
    To install matplotlib, use 'pip install matplotlib'
    """
    plt.style.use('ggplot')

    dictionary = bf.frequency(arr)
    keys = dictionary.keys()
    values = [dictionary[i] for i in keys]
    x_pos = [i for i in range(len(keys))]

    plt.bar(x_pos, values, color='green')
    plt.title("Graph of Frequencies")
    plt.xticks(x_pos, keys)
    plt.show()

def graph_scatter(arr):
    """
    This function returns a scatter plot of the given data
    Note that input array must be an array of array with each sub-array
    having two elements: [x,y] for the respective point
    """
    plt.style.use('ggplot')

    x = [i[0] for i in arr]
    y = [i[1] for i in arr]

    fig = plt.figure()
    axes = fig.add_axes([0,0,1,1])
    axes.scatter(x, y, color = 'green')
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_title('Scatter Plot of Given Points')
    plt.show()
