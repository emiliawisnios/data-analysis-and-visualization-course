import matplotlib.pyplot as plt
import numpy as np


def generate_plot(plot_dataframe, labels, year, colors, max_value, plot_title, plot_label, directory, number_of_countries=5):

    assert number_of_countries <= len(labels), 'Number of countries is bigger than number of countries in dataset'

    # creating plot
    fig, _ = plt.subplots()

    x_axis = np.arange(number_of_countries)

    plt.bar(x_axis, plot_dataframe, color=colors)

    # adding plot name and label
    plt.title(plot_title)
    plt.ylabel(plot_label)

    # setting plot labels and properties
    plt.xticks(x_axis, labels, rotation=45)

    plt.ylim(0, (max_value + 0.5 * max_value))
    # box for current year
    plt.text(3.25, (max_value + 0.2 * max_value), str(year), style='italic', size=30,
           bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    plt.tight_layout()

    plt.savefig(directory + str(year) + '.png')
    plt.close(fig)
