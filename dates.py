from dateutil import relativedelta
from datetime import datetime, timedelta
dt_now = datetime.now()
delta_day = timedelta(days = 1)
dt_yest = dt_now - delta_day
dt_mth_ago = datetime(dt_now.year, dt_now.month - 1, dt_now.day)
delta_month = relativedelta.relativedelta(months = 1)
dt_mth_ago2 = dt_now - delta_month


print(dt_now)
print(dt_yest)
print(dt_mth_ago)
print(dt_mth_ago2)

dates2 = '01/01/17 12:10:03.234567'
dt_dt = datetime.strptime(dates2,'%m/%d/%y %H:%M:%S.%f')

print(dt_dt)
