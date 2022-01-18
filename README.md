Covid-19 Visualization User Manual

Contributions: Andrew Chow, Joshua Jones, Yash Pandya, Chibuzor Okwusiuno



This visualization project consists of 3 main programs that can analyze and visualize
Covid-19 statistics among different areas in Ontario, including schools, prisons and vaccinations.



Program 1: Vaccines

This program finds the total number of Vaccinations among Ontario's senior population

Example:
    
    <python> <Vaccine/vaccine.py> <Vaccine/vaccinedoses.csv>
    
    This program will print the total vaccine information for every day since the 24th of December 2020 as well as information that displays the percentage of the senior population(65+) that is vaccinated, how many more seniors(65+) need to still be vaccinated and the amount of seniors(65+) that have currently been vaccinated.


To run use the shell command:

    <python> <Vaccine/vaccines.py> <Vaccine/vaccinedoses.csv>


To output the following vaccine data to a .txt file do the following steps:

    <python> <Vaccine/vaccine.py> <Vaccine/vaccinedoses.csv> > filename.txt

Graph the data to a pdf file:

    <python> <Vaccine/vaccine_plot.py> <Vaccine/vaccine.txt> <filename.pdf>



Program 2: Prisons

    This program finds the total number of Covid cases among institutions in Ontario within a certain time period from May 2020 to March 2021 (Present)

Example: 

    <python> <Prison/prisons.py> <Prison/prison_data.csv> <01> <03> 

    This program will total the covid cases among all regions from January to March

To run use the shell command: 

    <python> <Prison/prisons.py> <Prison/prison_data.csv> <XX> <YY> 

        XX: Start Month   needs a leading 0 for months January-September
        YY: End Enm Month needs a leading 0 for months January-September

To output the following case data within the time period to a graph, do the following steps:

    <python> <Prison/prisons.py> <Prison/prison_data.csv> <XX> <YY> > filename.txt

Graph the data to a pdf file:

    <python> <Prison/prison_plot.py> <filename.txt> <filename.pdf>





Program 3: Schools

    This program finds the total amount of Covid cases in schools from the beginning of the pandemic to present

Example:

    <python> <School/schools.py> <School/schoolcovidsummary.csv> 


To output the following school covid 19 data do the following steps:

    <python> <School/schools.py> <School/schoolcovidsummary.csv> > filename.txt

Graph the data to a pdf file:

    <python> <School/school_plot.py> <filename.txt> <filename.pdf>