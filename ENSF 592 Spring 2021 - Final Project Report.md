## ENSF 592 Spring 2021 - Final Project Report
Authors: Bhavyai Gupta, Brandon Attai
Date: 2021-06-15
Course: ENSF 592

# Summary 
This program allows a user to request, select or visualize various statistics surrounding United Nations Data to give insight into population and wealth trends for UN Regions, Sub-Regions and Countries. To achieve this, a total of four Datasets were used as follows:

* UN Region, Sub-Region and Country
* Population Growth, Fertility, Life Expectancy and Mortality
* Population in the Capital City, Urban and Rural Areas
* GDP and GDP per Capita

The program makes use of four Python files to provide an interactive command line user interface. The interface makes use of color-coded messages to allow for ease of readability. Once the user runs the `launch.python` file that contains main, the user is given a real time update on the steps being completed and their status via the terminal. After each step is completed, the user is updated with the status. The user is informed of information such as, the data being merged into one DataFrame and when the check for null values is completed. 

The user is then prompted to enter the program menu. Once entered, the user has 7 options to select from, which allows for exporting, requesting, selecting, or visualizing the statistics. For example, if the user wishes print the aggregate statistics for GDP per capita with respect to the USA or Ratio of Urban Population to GDP per Capita amongst others, the user can select option `[4]` and print the aggregate statistics for a Region or Sub-Region based on the user’s text entry. Below summarizes the other functionality within the program. 

* Print the imported datasets
* Re-export the entire merged hierarchical dataset into Excel
* Print aggregate stats for the entire dataset
* Print aggregation stats grouped by UN Region/UN Sub-Region and available years
* Print the list of countries that have higher GDP per capita than USA, and the year
* Show plot of Population Increase, Total Fertility Rate and Life Expectancy for a country
* Exit

The program makes use of object-oriented programming by using classes and methods to handle data analysis and calculations. Finally, exception handling is performed throughout the program to ensure the program does not terminate if the user enters an invalid input. 

# References
1. UN Region, Sub-Region and Country, Development Data Section of the Development Data and Outreach Branch within the Statistics Division of the Department of Economic and Social Affairs (UN DESA) of the UN Secretariat, June 2019. [Online]. Available:
https://data.un.org/_Docs/SYB/CSV/SYB63_1_202105_Population,%20Surface%20Area%20and%20Density.csv

2. Population Growth, Fertility, Life Expectancy and Mortality, Development Data Section of the Development Data and Outreach Branch within the Statistics Division of the Department of Economic and Social Affairs (UN DESA) of the UN Secretariat, Aug. 2019. [Online]. Available: 
https://data.un.org/_Docs/SYB/CSV/SYB62_246_201907_Population%20Growth,%20Fertility%20and%20Mortality%20Indicators.csv

3. Population in the Capital City, Urban and Rural Areas, Development Data Section of the Development Data and Outreach Branch within the Statistics Division of the Department of Economic and Social Affairs (UN DESA) of the UN Secretariat, May 2018. [Online]. Available:
https://data.un.org/_Docs/SYB/CSV/SYB61_253_Population%20Growth%20Rates%20in%20Urban%20areas%20and%20Capital%20cities.csv

4. GDP and GDP per Capita, Development Data Section of the Development Data and Outreach Branch within the Statistics Division of the Department of Economic and Social Affairs (UN DESA) of the UN Secretariat, Nov. 2020. [Online]. Available:
https://data.un.org/_Docs/SYB/CSV/SYB63_230_202009_GDP%20and%20GDP%20Per%20Capita.csv 




