from load import data_loading_and_parsing
from plot import generate_plot
import numpy as np
import random as rd


def gather_plot_data(dataframe):

    rd.seed()
    # choosing random year
    random_year = rd.randint(1960, 2019)
    # choosing random country
    random_country_index = rd.randint(0, len(dataframe.index))
    random_country_name = dataframe['Country Name'][random_country_index]
    dataframe.sort_values(by=str(random_year), ascending=False, inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    random_country_index = dataframe.index[dataframe['Country Name'] == random_country_name][0]
    indexes = []
    if random_country_index == 1:
        for i in range(random_country_index, random_country_index+5):
            indexes.append(i)
    elif random_country_index == 2:
        for i in range(random_country_index-1, random_country_index+4):
            indexes.append(i)
    elif 2 < random_country_index < len(dataframe.index)-2:
        for i in range(random_country_index-2, random_country_index+3):
            indexes.append(i)
    elif random_country_index == len(dataframe.index)-2:
        for i in range(random_country_index-3, random_country_index+2):
            indexes.append(i)
    else:
        for i in range(random_country_index-4, random_country_index+1):
            indexes.append(i)

    plot_data = dataframe.loc[indexes, :]
    row_names = np.array(plot_data['Country Name'])
    years = []
    for i in range(1960, 2020):
        years.append(str(i))

    return plot_data, row_names, years, random_country_name, random_year


path = 'data/population_data.csv'
population_data = data_loading_and_parsing(path)
data, labels_x, years, country, year = gather_plot_data(population_data)
color_set = ['#a6dba0', '#5aae61', '#1b7837', '#00441b', '#40004b', '#762a83', '#9970ab', '#c2a5cf']
max_value = data[years[len(years)-1]].max()
for k in range(1, len(data.columns)):
    current_data = np.array(data[years[k-1]])
    plot_title = 'The evolution of populations of countries that were most \n' + 'similar population-wise to ' + \
                 country + ' in ' + str(year)
    plot_label = 'Population [unit]'
    generate_plot(current_data, labels_x, years[k - 1], color_set, max_value, plot_title, plot_label, 'B/')
