import pandas as pd


def data_loading_and_parsing(file_path):
    raw_population_data = pd.read_csv(file_path, skiprows=4)

    # last two columns are empty so we delete it

    population_data = raw_population_data.iloc[:, :-2]

    # dropping useless columns

    cols = ['Indicator Name', 'Indicator Code']
    population_data.drop(cols, inplace=True, axis=1)

    # dropping rows which are not countries

    not_countries = ['Aruba', 'American Samoa', 'Arab World', 'Bermuda', 'British Virgin Islands', 'North America',
                     'Caribbean small states', 'Cayman Islands', 'Central Europe and the Baltics', 'Channel Islands',
                     'Curacao', 'Early-demographic dividend', 'East Asia & Pacific', 'Low & middle income',
                     'East Asia & Pacific (excluding high income)', 'East Asia & Pacific (IDA & IBRD countries)',
                     'Euro area', 'Europe & Central Asia', 'Europe & Central Asia (excluding high income)',
                     'Europe & Central Asia (IDA & IBRD countries)', 'European Union', 'Faroe Islands', 'Low income',
                     'Fragile and conflict affected situations', 'French Polynesia', 'Gibraltar', 'Greenland', 'Guam',
                     'Heavily indebted poor countries (HIPC)', 'High income', 'Hong Kong SAR, China', 'IBRD only',
                     'IDA & IBRD total', 'IDA blend', 'IDA only', 'IDA total', 'Isle of Man', 'Lower middle income',
                     'Late-demographic dividend', 'Latin America & Caribbean', 'Macao SAR, China', 'Puerto Rico',
                     'Latin America & Caribbean (excluding high income)', 'Middle East & North Africa',
                     'Latin America & the Caribbean (IDA & IBRD countries)', 'Middle income', 'New Caledonia',
                     'Least developed countries: UN classification', 'Northern Mariana Islands', 'Not classified',
                     'Middle East & North Africa (excluding high income)', 'OECD members', 'Other small states',
                     'Middle East & North Africa (IDA & IBRD countries)', 'Pacific island small states',
                     'Post-demographic dividend', 'Pre-demographic dividend', 'Sint Maarten (Dutch part)',
                     'Small states', 'South Asia', 'South Asia (IDA & IBRD)', 'St. Kitts and Nevis', 'St. Lucia',
                     'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Sub-Saharan Africa', 'World',
                     'Sub-Saharan Africa (excluding high income)', 'Sub-Saharan Africa (IDA & IBRD countries)',
                     'Turks and Caicos Islands', 'Upper middle income', 'Virgin Islands (U.S.)', 'West Bank and Gaza']

    index_names = population_data[population_data['Country Name'].isin(not_countries)].index
    population_data.drop(index_names, inplace=True)

    # fixing inconsistencies in data

    fixed_countries = [['Bahamas, The', 'The Bahamas'], ['Egypt, Arab Rep.', 'Egypt'], ['Gambia, The', 'Gambia'],
                       ['Iran, Islamic Rep.', 'Iran'], ['Micronesia, Fed. Sts.', 'Micronesia'],
                       ['Venezuela, RB', 'Venezuela'], ['Yemen, Rep.', 'Yemen'], ['Lao PDR', 'Laos'],
                       ['Kyrgyz Republic', 'Kyrgyzstan'], ['Korea, Dem. People’s Rep.', 'North Korea'],
                       ['Korea, Rep.', 'South Korea'], ['Congo, Dem. Rep.', 'Democratic Republic of the Congo'],
                       ['Congo, Rep.', 'Congo'], ['Russian Federation', 'Russia']]

    for i in range(len(fixed_countries)):
        population_data['Country Name'] = population_data['Country Name'].replace([fixed_countries[i][0]],
                                                                                  fixed_countries[i][1])

    # fixing indexes after dropping rows
    population_data.reset_index(drop=True, inplace=True)

    return population_data
