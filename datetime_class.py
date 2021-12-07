""" Date and Time in Python 3 """
# import string
from datetime import time , date , datetime ,timedelta
# from datetime import date
# from datetime import time
# from datetime import datetime as dt

# year_of_birth = int(input("Enter the year of your birth : "))
# month_of_birth = int(input("Enter the month of your birth : "))
# day_of_birth = int(input("Enter the day of your birth : "))
# print(f"Full Date of birth : {day_of_birth}/{month_of_birth}/{year_of_birth}")

# dob = date(year_of_birth , month_of_birth , day_of_birth)
date_now = date.today()


# delta_age = date_now - dob
# real_age = delta_age.days // 365
# print(str(real_age) + "yrs")
print(f"{date_now:%A/%b/%Y , %j}")
# print(age)

# start_time = time(23 , 12 , 34, 67)
# start_date = date(2011, 12, 23)
# print(start_date)
# print(start_time)

















#yyyy/mm/dd
# print(time(12 , 23 , 56))
# print(date.today())
# present_moment = dt.now()
# print(present_moment.time())
# print(present_moment.date())

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.punctuation)
