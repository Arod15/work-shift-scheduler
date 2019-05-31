import openpyxl as op
import datetime
from openpyxl.styles import PatternFill

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

filename = 'work-sample.xlsx'
workbook = op.load_workbook(filename)
sheet1 = workbook.active

def color_row(r):
  for i in range(1, sheet1.max_column):
    sheet1.cell(row=r, column=i).fill = PatternFill(bgColor="FFC7CE", fill_type = "solid")
def sum_hours(r):
  total = 0
  for i in range(1, 8):
    total += sheet1.cell(row=r, column=7).value
  sheet1.cell(row=r+8, column=7).value = total
def calc_hours(r):
  return
def shifts(row, num):
  col = 0
  for i in range(num):
    sheet1.cell(row=row, column=(3+(num*i))).value = 'Start'
    sheet1.cell(row=row, column=(4+(num*i))).value = 'End'
    if i == num-1:
      col = 5 + (num * i)
  sheet1.cell(row=row, column=col).value = 'Hours'
def week(row):
  for i in range(len(days)):
    sheet1.cell(row=row+i, column=1).value = days[i]
def dates(row, col):
  start_date = sheet1.cell(row=row, column=col).value
  for i in range(1, len(days)):
    start_date += datetime.timedelta(days=1)
    sheet1.cell(row=row+i, column=col).value = start_date
def init(r, c, start=None):
  sheet1.cell(row=r, column=1).value = 'Day'
  sheet1.cell(row=r, column=2).value = 'Date'
  shifts(r, 2)
  week(r+1)
  if start is None:
    sheet1.cell(row=r+1, column=2).value = datetime.date(datetime.date.today().year, 5, 26)
  else:
    sheet1.cell(row=r+1, column=2).value = start
  dates(r+1, 2)
  color_row(r+8)
def print_sheet(maxr, maxc):
  for i in range(1, maxr+1):
    for j in range(1, maxc+1):
      print(i, j, sheet1.cell(row=i, column=j).value)
def main():
  i = 1
  day_date = datetime.date.today()
  while sheet1.cell(row=i, column=1).value is not None:
    day_date = sheet1.cell(row=i, column=2).value
    i += 1
  i += 1
  start_date = day_date + datetime.timedelta(days=1)
  init(i, 1, start=start_date)

if sheet1.cell(row=1, column=1).value is None:
  init(1, 1)
# else:
  main()

print_sheet(sheet1.max_row, sheet1.max_column)

workbook.close()
