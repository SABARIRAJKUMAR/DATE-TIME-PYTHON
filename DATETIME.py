import datetime as dt

current_date = dt.date.today()
print("current date :", current_date)

new = dt.date(2021, 10, 25)
print(new)
print("year:", new.year)
print("month:", new.month)
print("day:", new.day)

print("----------------------------")

a = dt.time(10, 44, 9, 4600)
print(a)
print("hour:", a.hour)
print("minute:", a.minute)
print("second:", a.second)
print("microsecond:", a.microsecond)

print("------------------------------")

current_time=dt.datetime.now()
print("current time:", current_time)

print("------------------------------")

new= dt.datetime(2021,5,31,12,5,10)
print(new)
print(new.date())
print(new.time())

print("------------------------------")

current = dt.datetime.now()
new_year = dt.datetime(2023,1,1)
difference =new_year - current
print(difference)

print("------------------------------")

current = dt.datetime.now()
print(current)
s= current.strftime("%A %b %d %Y")
print(s)


