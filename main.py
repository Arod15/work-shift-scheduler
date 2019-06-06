import datetime
from functions import *

zero_time = datetime.time(hour=0, minute=0, second=0)

filename = 'init.xlsx'
# filename = 'new-init.xlsx'
workbook = op.load_workbook(filename)
sheet1 = workbook.active

def log_hours(date, time):
  insert_hours(time[0], time[1], date, sheet1)
def show_sheet():
  print_sheet(sheet1)

# def check_hours(date):
#   row = 0
#   col = 0
#   times = []
#   for i in range(2, sheet1.max_row+1):
#     row = i
#     if sheet1.cell(row=i, column=2).value == date:
#       break
#   for j in range(2, sheet1.max_column):
#     col = j


def test1():
  start = datetime.time(hour=1, minute=30)
  end = datetime.time(hour=4, minute=45)
  time_now = datetime.datetime.combine(date, zero_time)
  curr_date = time_now
  for x in range(sheet1.max_row): 
    insert_hours(start, end, curr_date, sheet1)
    curr_date += datetime.timedelta(days=1)
def date_parser():
  date = input('Date (MM/DD/YYYY): ')
  date_array = date.split('/')
  try:
    date = datetime.date(int(date_array[2]), int(date_array[0]), int(date_array[1]))
  except:
    print('Enter valid date')
    return False
  return datetime.datetime.combine(date, zero_time)
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
    return False
  return (start, end)
def main1():
  date = date_parser()
  if date == False:
    return False 
  time = time_parser()
  if time == False:
    return False
  initialize(sheet1)
  log_hours(date, time)

# main1()
test1()
# print_sheet(sheet1)

workbook.save('new-' + filename)
# workbook.save(filename)
workbook.close()