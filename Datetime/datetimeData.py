from datetime import datetime
import pytz

'''
1) Given the following two dates, which correspond to the dates of birth of two siblings (in the Europe/Madrid time zone), 
indicate the difference between them in days, hours, minutes and seconds
'''

son1 = datetime(1985, 10, 20, 17, 55)
son2 = datetime(1992, 6, 25, 18, 30)

difference = son2 - son1
print("Difference =", difference)

'''
2) Create a function called formato_fecha() that receives a date of type datetime as a parameter and returns the following format: "20 de Abril del 2020".
In many occasions our systems are configured by default in English, and it is not possible to change the locale to Spanish. Therefore, we have to learn how to 
select and display the months in Spanish even if our system is in English or another language. Create a tuple to store the list of months in Spanish in order to 
select the appropriate month name based on a date we provide to the program. It is forbidden to use methods such as locale, setlocale or strftime.
Test the function by sending it a date predefined by you and the current date (now).
'''

dt1 = datetime.now()
dt2 = datetime(2019, 2, 28)

months = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

def date_format(dt, dt_month):
    month_spanish = months[(dt_month)-1]
    print(dt.strftime("%d"), "de", month_spanish, "del", dt.strftime("%Y"))  # print the day, month and year in Spanish format

date_format(dt1, dt1.month)
date_format(dt2, dt2.month)

'''
3) Using strftime and format the current date to the following format (without the dots):

Day: 20
Month: 04
Year: 2020
Hour: 16
Minutes: 19
Seconds (and microseconds): 08.879057
'''

dt = datetime.now()
day = dt.strftime("%d")
month = dt.strftime("%m")
year = dt.strftime("%Y")
hour = dt.strftime("%H")
minutes = dt.strftime("%M")
seconds = dt.strftime("%S")
microseconds = dt.strftime("%f")

print("Day:", day, "\nMonth:", month, "\nYear:", year, 
      "\nHour:", hour, "\nMinutes:", minutes, "\nSeconds (and microseconds):", seconds+"."+microseconds)