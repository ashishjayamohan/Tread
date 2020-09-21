import matplotlib.pyplot as plt

import basic_functions as bf

def graph_frequency_histogram(arr, bar_color='green', title='Graph of Frequencies'):
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

    plt.bar(x_pos, values, color=bar_color)
    plt.title(title)
    plt.xticks(x_pos, keys)
    plt.show()

def graph_scatter(arr, color='green', title='Scatter Plot of Given Points', x_label='X', y_label='Y'):
    """
    This function returns a scatter plot of the given data
    Note that input array must be an array of array with each sub-array
    having two elements: [x,y] for the respective point
    """
    plt.style.use('ggplot')

    x, y = [], []
    for point in arr:
        x.append(point[0])
        y.append(point[1])

    fig = plt.figure()
    axes = fig.add_axes([0,0,1,1])
    axes.scatter(x, y, color=color)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    axes.set_title(title)
    plt.show()
