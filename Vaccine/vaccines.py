#!/usr/bin/env python

'''
vaccine.py
  Author(s): Yash Pandya (1146824), Chibuzor Okwusiuno(1123349), Joshua Jones(1125364), Andrew Chow (1088114)

  Earlier Contributors: Andrew Hamilton-Wright

  Project: Lab Assignment 7 Script (Iteration 0)
  Date of Last Update: Mar 30, 2021.

  Functional Summary
      vaccine.py demonstrates how we can
      use vaccine data to track the progress and speed of the vaccine distributions within the senior population

     Commandline Parameters: 1
        argv[0] = data file
        argv[1] = csv file
'''


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# command line parameters, as well as standard input, output and error
import csv

#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
# This is a dictionary -- a data structure that associates
# values (in this case integers) with names.

INDEX_MAP = {
        "report_date" :  0,
        "previous_day_doses_administered" :  1,
        "total_doses_administered" :  2,
        "total_doses_in_fully_vaccinated_individuals" :  3,
        "total_individuals_fully_vaccinated" :  4
        }


def main(argv):
    '''
    Load a data file and print out the columns matching the selected
    indices
    '''

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 2:
        print("Usage: vaccine.py <data file>>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)
    # only one argument for command line 
    filename = argv[1]

    # print out the specified index column from our sample data
    try:
        fh = open(filename, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                filename, err), file=sys.stderr)
        sys.exit(1)

    data_reader = csv.reader(fh)
      
    ## iterate through the rows
    row_number = 0
    report_date = []
    total_individuals_fully_vaccinated = []
    percentage_vaccinated = 0
    difference_vaccinated = 0
    
    # Add URL in order to update vaccine doses frequently 
  
    for row_number, row in enumerate(data_reader):
      if row_number > 0:
        total_vaccinated = row[INDEX_MAP["total_individuals_fully_vaccinated"]]
        current_date = row[INDEX_MAP["report_date"]]
        
        
        report_date.append(current_date)
        total_individuals_fully_vaccinated.append(total_vaccinated.replace(",",""))
    print("{},{}".format("date","total"))
    length = len(report_date)
    for i in range(length):
    
      
      print(" {},{} ".format(report_date[i],total_individuals_fully_vaccinated[i]))

    report_date.reverse()           
    #print(report_date[0])

    total_individuals_fully_vaccinated.reverse()           
    #print(total_individuals_fully_vaccinated[0])

    print("\n")
    
    print("The amount of senior citizens that have currently been vaccinated in Ontario is {} people\n".format(total_individuals_fully_vaccinated[0]))

    percentage_vaccinated = int(total_individuals_fully_vaccinated[0])/2594358 * 100
    print("The percentage of the senior citizen population that is vaccinated in ontario is {:.2f}%\n".format(percentage_vaccinated))

    difference_vaccinated = 2594358 - int(total_individuals_fully_vaccinated[0])
    print("The amount of senior citizens that still need to be vaccinated in Ontario is {} people\n".format(difference_vaccinated))
       

##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
