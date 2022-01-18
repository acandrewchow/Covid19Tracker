#!/usr/bin/env python

'''
schools.py
  Author(s): Yash Pandya, Chibuzor Okwusiuno, Joshua Jones, Andrew Chow

  Functional Summary
      schools demonstrates how we can use school covid cases and testing data to analyze the current trends in Covid-19 daily

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
        "collected_date" :  0,
        "reported_date" :  1,
        "current_schools_w_cases" :  2,
        "current_schools_closed" :  3,
        "current_total_number_schools" : 4,
        "new_total_school_related_cases" :  5,
        "new_school_related_student_cases" :  6,
        "new_school_related_staff_cases" :  7,
        "new_school_related_unspecified_cases" :  8,
        "recent_total_school_related_cases" :  9,
        "recent_school_related_student_cases" :  10,
        "recent_school_related_staff_cases,recent_school_related_unspecified_cases" :  11,
        "past_total_school_related_cases,past_school_related_student_cases" :  12,
        "past_school_related_staff_cases" :  13,
        "past_school_related_unspecified_cases" :  14,
        "cumulative_school_related_cases" :  15,
        "cumulative_school_related_student_cases" :  16,
        "cumulative_school_related_staff_cases" :  17,
        "cumulative_school_related_unspecified_cases" :  18,
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
        print("Usage: schools.py <data file>>")

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
    total_cases = []
    
    
    # Add URL in order to update vaccine doses frequently 
  
    for row_number, row in enumerate(data_reader):
      if row_number > 0:
        current_cases = row[INDEX_MAP["new_total_school_related_cases"]]
        current_date = row[INDEX_MAP["reported_date"]]
        
        
        report_date.append(current_date)
        total_cases.append(current_cases)
    print("{},{}".format("Reported Date","Total Cases"))
    length = len(report_date)
    for i in range(length):
      
      print(" {},{} ".format(report_date[i],total_cases[i]))
      
##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
