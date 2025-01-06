from datetime import datetime as dt
import calendar

arr = input().split()
month = {name: x for x, name in enumerate(calendar.month_name)}[arr[0]]
day = int(arr[1][:-1])
year = int(arr[2])
hh, mm = map(int, arr[3].split(':'))

start = dt(year, 1, 1)
whole = (dt(year+1, 1, 1) - start).total_seconds()
current = (dt(year, month, day, hh, mm) - start).total_seconds()

print(current / whole * 100)

# dt.strptime을 사용하면 더 편함