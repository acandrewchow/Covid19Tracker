#!/usr/bin/env python

'''
vaccine.py
  Author(s): Yash Pandya, Chibuzor Okwusiuno, Joshua Jones, Andrew Chow

  Functional Summary
      prisons.py displays the visualization and information required to compare two different time periods of Covid-19 among
      many different insitutions in Ontario. In addition, the user is able to select specific regions upon the command line
      when running the system to display cases for that specific institute.

     Commandline Parameters: 4
        argv[0] = data file
        argv[1] = csv file
        argv[2] = start date
        argv[3] = end date

  
        
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
        "_id" :  0,
        "Reported_Date" :  1,
        "Region" :  2,
        "Institution" :  3,
        "Total_Active_Inmate_Cases_As_Of_Reported_Date" :  4,
        "Cumul_Nr_Resolved_Inmate_Cases_As_Of_Reported_Date" :  5,
        "Cumul_Nr_Positive_Released_Inmate_Cases_As_Of_Reported_Date" :  6,
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
    if len(argv) != 4:
        print("Usage: prisons.py <data file>>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)
    # only one argument for command line 
    filename = argv[1]
    start_date = argv[2]
    end_date = argv[3]
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
    Report_Date = []
    Region = []
    accurate_report_date = []
    Total_Active_Cases = []
    Central_Total = 0
    
    Toronto_Total = 0
    Western_Total = 0
    Eastern_Total= 0
    Central_Total = 0
    Northern_Total = 0


    for row_number, row in enumerate(data_reader):
      if row_number > 0:
        Total_Active_Case = row[INDEX_MAP["Total_Active_Inmate_Cases_As_Of_Reported_Date"]]
        Current_Date = row[INDEX_MAP["Reported_Date"]]
        Current_Region = row[INDEX_MAP["Region"]]

        Report_Date.append(Current_Date)
        Total_Active_Cases.append(Total_Active_Case)
        Region.append(Current_Region)

        seen = set(accurate_report_date)
        if Current_Date not in seen:
          seen.add(Current_Date)
          accurate_report_date.append(Current_Date)

 
    #for i in range(length) :
      #print("{},{},{}".format(Report_Date[i],Region[i],#Total_Active_Cases[i])
    final_dates = []
    counter = 0
    
    for x in accurate_report_date:
      counter += 1
      a,b,c = x.split("-")

      if b == start_date:
        break

    start = counter - 1

    counter = 0
    
    for x in accurate_report_date:
      counter += 1
      a,b,c = x.split("-")

      if b == end_date:
        break

    end = counter - 1
      
    for i in range(start, end):
      final_dates.append(accurate_report_date[i])
      #print(final_dates)
    print("{},{},{}".format("Date", "Region", "Cases")) 
    for x in final_dates:
      northern = 0
      western = 0
      eastern = 0
      toronto = 0
      central = 0
     
      length = len(Report_Date)
      for i in range(length):
          
        if x == Report_Date[i]:
            #index = all_episode_dates.index(y)
            #print(index)
          if(Region[i] == "Toronto"):
            toronto = toronto + int(Total_Active_Cases[i])
          if(Region[i] == "Central"):
            central = central + int(Total_Active_Cases[i])
          if(Region[i] == "Eastern"):
            eastern = eastern + int(Total_Active_Cases[i])
          if(Region == "Western"):
            western = western + int(Total_Active_Cases[i])
          if(Region[i] == "Northern"):
            northern = northern + int(Total_Active_Cases[i])
      print("{},{},{}".format(x,  "Toronto", toronto)) 
      print("{},{},{}".format(x, "Central", central)) 
      print("{},{},{}".format(x, "Eastern", eastern)) 
      print("{},{},{}".format(x, "Western", western)) 
      print("{},{},{}".format(x, "Northern", northern)) 

    print("\n")
    print("Total Cases Per Region from", argv[2], "to", argv[3])
    print("Toronto Region:", toronto, "cases")
    print("Central Region:", central, "cases")
    print("Eastern Region:", eastern, "cases")
    print("Western Region:", western, "cases")
    print("Northern Region:", northern, "cases")

##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
