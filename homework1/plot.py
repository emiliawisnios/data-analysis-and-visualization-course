import matplotlib.pyplot as plt
import numpy as np


def generate_plot(plot_dataframe, labels, year, colors, plot_title, plot_label, directory, number_of_countries=5):

    assert number_of_countries <= len(labels), 'Number of countries is bigger than number of countries in dataset'

    # creating plot
    fig, _ = plt.subplots()

    x_axis = np.arange(number_of_countries)
    y_axis = np.arange(10) * 200000000

    # scaling labels
    y_labels = []
    for i in range(len(y_axis)):
        y_labels.append(np.round(i * 0.2, 1))

    plt.bar(x_axis, plot_dataframe, color=colors)

    # adding plot name and label
    plt.title(plot_title)
    plt.ylabel(plot_label)

    # setting plot labels and properties
    plt.xticks(x_axis, labels, rotation=45)
    plt.yticks(y_axis, y_labels)

    plt.ylim(0, 1500000000)

    # box for current year
    plt.text(3.25, 1200000000.0, str(year), style='italic', size=30,
             bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    plt.tight_layout()

    plt.savefig(directory + str(year) + '.png')
    plt.close(fig)
