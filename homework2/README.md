Animated plots part 2
=====================================

We use again the same file from the World Bank:
https://data.worldbank.org/indicator/SP.POP.TOTL?end=2018&start=1960&view=chart

In the previous exercise, we selected the data for:
<br>
a) 5 most populated countries
<br>
b) 5 randomly picked 
<br>
c) 5 with Poland as the centroid

* * *

IMPORTANT: For animation plots use as much as possible "matplotlib.animation"
https://matplotlib.org/3.2.0/api/animation_api.html

Remember, we use English. All text used in the plots should be English.

* * *

I) Playing with colors and labels:
<br>
For all plots from exercise 2 (a-c) do bar plots:
<br>
a) color version (most likely you already have a good starting point)
<br>
b) black & white version

Requirements:
- on top of each bar put three letter "Country Code" e.g. CHN for China
- "Country Code" position is updated with respect to the bar size
- for black and white version use shapes and/or textures to indicate the classification
- the axis indicating the population should be fixed 
  (the bar should show the increase, not the lidership)
- there is year counter inside of the plot (make it big enough)
- the font for all elements should be visible (from a large distance)
- increase the readiness of the plot as much as possible 
(e.g. do not use 150.000.000, 150e6 on the scale; 150M is much shorter and easy to read)

Expected result: 6 animated bar plots (gif; 3 b&w and 3 color)

* * *

II) Play with a different representation of the data:

All of the plots so far had been "bar plots". Now, the task is to present the data using different plot representation. For each a-c from previous lab do similar animated plots, but as:
<br>
A) line plot (so the plots start as a dot and the line moves while the time progress)
<br>
B) bubble plot (x is time, y is the population, z (bubble) is a population density) 
<br>
C) any other representation

- find the data about the area related to the countries of interest and calculate 
population density (population/area).

Requirements:
- on top of each bar, line or bubble put three-letter "Country Code" e.g. CHN for China
- "Country Code" position is updated with the respect to the line or bubble location
- there is year counter inside of the plot (make it big enough)
- the font for all elements should be visible (from a large distance)

Expected result: 3 animated, color plots (gif)

* * *

Homework: Extend the html from the last lab by 9 plots from part I and 3 plots from part II and send the results as usual till the end of 28.03.2021. 
