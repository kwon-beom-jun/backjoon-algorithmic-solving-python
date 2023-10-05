import datetime as dt

now = dt.datetime.now() + dt.timedelta(hours=9)

print(str(now.year) + "\n" + str(now.month) + "\n" + str(now.day))