import matplotlib.pyplot as plt
import numpy as np


def generate_plot(plot_dataframe, labels, year, colors, max_value, plot_title, plot_label, directory, number_of_countries=5):

    assert number_of_countries <= len(labels), 'Number of countries is bigger than number of countries in dataset'

    # creating plot
    fig, ax = plt.subplots()

    x_axis = np.arange(number_of_countries)

    plt.bar(x_axis, plot_dataframe, color=colors)

    ticks = ax.get_yticks()

    order_of_max = len(str(int(max_value)))
    order_of_label = len(str(int(ticks[number_of_countries - 1])))

    print(max_value)
    print(ticks)
    print(order_of_max - order_of_label)

    if order_of_max == 6:
        if order_of_max - order_of_label < 2:
            unit_name = 'thousands'
        elif order_of_max - order_of_label > 1:
            unit_name = 'houndreds of thousands'
    elif order_of_max == 7:
        if order_of_max - order_of_label < 3:
            unit_name = 'millions'
        elif order_of_max - order_of_label > 1:
            unit_name = 'tens of millions'
    elif order_of_max == 8:
        if order_of_max - order_of_label < 2:
            unit_name = 'tens of millions'
        elif order_of_max - order_of_label > 1:
            unit_name = 'hundreds of millions'
    elif order_of_max == 9:
        if order_of_max - order_of_label < 2:
            unit_name = 'hundreds of millions'
        elif order_of_max - order_of_label > 1:
            unit_name = 'billions'
    elif order_of_max == 10:
        if order_of_max - order_of_label < 2:
            unit_name = 'billions'
        elif order_of_max - order_of_label > 1:
            unit_name = 'tens of billions'

    new_plot_label = plot_label.replace('unit', unit_name)

    # setting plot labels and properties
    plt.xticks(x_axis, labels, rotation=45)

    plt.ylim(0, (1.5 * max_value) )
    # box for current year
    plt.text(3.25, (max_value + 0.2 * max_value), str(year), style='italic', size=30,
           bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})


    # adding plot name and label
    plt.title(plot_title)
    plt.ylabel(new_plot_label)

    plt.tight_layout()

    plt.savefig(directory + str(year) + '.png')
    plt.close(fig)
 
