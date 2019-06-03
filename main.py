import datetime
from functions import *

def log_hours():
  date = date_parser()
  time = time_parser()
  insert_hours(time[0], time[1], date)

def date_parser():
  date = input('Date (MM/DD/YYYY): ')
  date_array = date.split('/')
  cons_date = None
  try:
    cons_date = datetime.date(int(date_array[2]), int(date_array[0]), int(date_array[1]))
  except:
    print('Enter valid date')
    return
    # date_parser()
  return cons_date
def time_parser():
  start = input('Time End (HH:MM): ')
  end = input('Time End (HH:MM): ')
  start_arr = start.split(':')
  end_arr = end.split(':')
  try:
    start = datetime.time(hour=int(start_arr[0]), minute=int(start_arr[1]))
    end = datetime.time(hour=int(end_arr[0]), minute=int(end_arr[1]))
  except:
    print('Enter valid time')
    time_parser()
  return (start, end)
def main1():
  log_hours()

main1()
print_sheet()