import pandas as pd
from load import data_loading_and_parsing
from plot import generate_plot
import numpy as np


def gather_plot_data(dataframe, number_of_countries=5):
    country_names = []  # list of five most populated countries for each year
    for i in range(1960, 2020):
        column_name = str(i)
        five_largest = dataframe.nlargest(5, column_name)
        country_array = five_largest['Country Name'].to_numpy()
        record = [column_name]
        for j in range(number_of_countries):
            record.append(country_array[j])
        country_names.append(record)

    years = []  # years 1960 - 2019 in string format
    index = []  # list of all most populated countries, may have repetitions

    for idx in range(len(country_names)):
        year = country_names[idx][0]
        years.append(year)
        for i in range(1, number_of_countries + 1):
            index.append([int(population_data[population_data['Country Name'] == country_names[idx][i]].index[0]),
                          country_names[idx][i]])

    unique_index = [list(x) for x in set(tuple(x) for x in index)]  # list of all most populated countries without repetitions

    population_values = []  # list of population values for each country (one list corresponds to one country)

    for i in range(len(unique_index)):
        single_record = [i]
        for idx in range(len(country_names)):
            year = country_names[idx][0]
            single_record.append(population_data.at[unique_index[i][0], year])
        population_values.append(single_record)

    population_values_array = np.array(population_values)  # one list corresponds to one country

    row_names = []  # list of country names

    for i in range(len(unique_index)):
        row_names.append(unique_index[i][1])

    col_names = ['Color index']  # numerical column for further color assignment

    for i in range(len(years)):
        col_names.append(years[i])

    plot_data = pd.DataFrame(population_values_array, index=row_names, columns=col_names)

    return plot_data, row_names, years


path = 'data/population_data.csv'
color_set = ['#a6dba0', '#5aae61', '#1b7837', '#00441b', '#40004b', '#762a83', '#9970ab', '#c2a5cf']
population_data = data_loading_and_parsing(path)
data, labels_x, years = gather_plot_data(population_data)

for k in range(1, len(data.columns)):
    current_colors = []
    copy_of_data = data.copy(deep=True)
    copy_of_data.sort_values(by=[years[k - 1]], ascending=False, inplace=True)
    head = copy_of_data.head(n=5)
    current_labels = np.array(head.index)
    current_data = np.array(head[years[k - 1]])
    color_idx = np.array(head['Color index'])
    for m in range(len(color_idx)):
        current_colors.append(color_set[int(color_idx[m])])

    # plot for given year
    generate_plot(current_data, current_labels, years[k - 1], current_colors, 'Most populous countries in years 1960 '
                                                                              '- 2019', 'Population [billion]', 'A/')
