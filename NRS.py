""" Nigerian Retirement System Program """

""" If user is within the range the age of 18 - 25 , then user should spend 35yrs in service , if the user is above that range , the user should retire at the 60yrs"""
from datetime import datetime as dt
from datetime import timedelta

# Variables
print("Welcome User \n Login or Signup : " , end="")
status = input().lower()
firstname = input("Enter your first name : ")
lastname = input("Enter your last name : ")

age = int(input("Enter your age : "))



years_to_serve = 0
def age_check(age):
    """ Returns the total number of years the employee has to serve the company """
    if age in range(18, 26):
        years_to_serve = 35
    else:
        years_to_serve = 60 - age
    return years_to_serve

def date_of_retirement(status , years_ts):
    dj = status_check(status)
    if "log" in status or "logged" in status:
        days_to_retirement = years_ts * 365 # get the number of days to work for e.g 12345 days
        days_to_retirement_date = dj + timedelta(days=days_to_retirement) # convert to date # 12/03/2045
        return days_to_retirement_date.date() , dj
    else:
        days_to_retirement = years_ts * 365 # get the number of days to work for e.g 12345 days
        days_to_retirement_date = dt.today() + timedelta(days=days_to_retirement) # convert to date # 12/03/2045
        return days_to_retirement_date.date() , dj
        
    

def status_check(status):
    if "log" in status or "logged" in status:
        day = int(input("Enter the day number you were employeed : "))
        month = int(input("Enter the month number you were employeed : "))
        year = int(input("Enter the year you were employeed : "))
        employment_date = dt(year , month , day)
    else:
        employment_date = dt.today().date()
    return employment_date

def main(status):
    yts = age_check(age)
    data = date_of_retirement(status, yts)
    date_joined = data[1]
    retire_date = data[0]
    
    return f"""
                                        User | {firstname} , {lastname} |
            Status        :          {status}
            Age           :          {age}
            Date Joined   :          {date_joined.date()}
            Retirement Date :        {retire_date}
"""
print(main(status))
