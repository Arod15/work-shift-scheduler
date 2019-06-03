import datetime
from functions import *

def log_hours():
  date = input('Date (MM/DD/YYYY): ')
  date_array = date.split('/')
  try:
    cons_date = datetime.date(int(date_array[2]), int(date_array[0]), int(date_array[1]))
  except:
    print('Enter valid date')
    log_hours()
def main1():
  log_hours()
main1()
print_sheet()