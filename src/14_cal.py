"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

if __name__ == "__main__":
    error_str = "Invalid format - format of arguments should be"
    error_str += "in form `[month [year]]` where `month` and `year` are both"
    error_str += "optional, but `year` requires `month` argument."
    args = sys.argv
    if len(args) > 3:
        print(error_str)
        exit()
    year = datetime.now().year
    month = datetime.now().month
    if len(args) > 1:
        try:
            month = int(args[1])
            assert(month < 13 and month > 0)
        except:
            print(error_str)
            exit()
    if len(args) > 2:
        try:
            year = int(args[2])
        except:
            print(error_str)
            exit()
    cal = calendar.TextCalendar()
    cal.prmonth(year, month)
