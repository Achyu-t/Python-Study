import datetime

date = datetime.date(2004, 2, 29)
today = datetime.date.today()

print(date)
print(today)

time = datetime.time(22 , 7 , 00)
time_now = datetime.datetime.now()

# time_now = time_now.strftime('%H:%M:%S %d-%m-%Y')           # Format date time into a string

# print(time , end = ' ')
print(time_now)


target_datetime = datetime.datetime(2020, 1,2,12,30,1)

current_datetime = time_now

if target_datetime < current_datetime:
    print("The Date is Passed.")

else:
    print("The target date has not passed")