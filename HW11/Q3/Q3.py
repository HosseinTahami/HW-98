import datetime
import jdatetime

def seconds_between_dates(date_str1, date_str2):
    date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
    delta = date2 - date1
    return abs(delta.total_seconds())

def leap_years_between_dates(date_str1, date_str2):
    year1 = int(date_str1.split('-')[0])
    year2 = int(date_str2.split('-')[0])
    count = 0
    for year in range(year1, year2+1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            count += 1
    return count

def daylight_savings_time(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    _, month, day = map(int, date_str.split('-'))
    dst_start, dst_end = None, None
    
    if month < 3 or (month == 3 and day < 8):
        dst_start = datetime.datetime(date.year, 3, 8)
    else:
        dst_start = datetime.datetime(date.year+1, 3, 8)
    if month > 10 or (month == 10 and day >= 25):
        dst_end = datetime.datetime(date.year, 10, 25)
    else:
        dst_end = datetime.datetime(date.year-1, 10, 25)

    if dst_start <= date < dst_end:
        return "1 hour forward"
    elif dst_end <= date < dst_start+datetime.timedelta(days=7):
        return "1 hour backward"
    else:
        return "no daylight savings time"

def convert_to_jalali(date_str):
    date = datetime.datetime.strptime(date_str,'%Y-%m-%d')
    jalali_date = jdatetime.datetime.fromgregorian(datetime=date).strftime("%Y-%m-%d")
    return jalali_date

date_str1 = input("Enter first date (YYYY-MM-DD): ")
date_str2 = input("Enter second date (YYYY-MM-DD): ")

seconds = seconds_between_dates(date_str1, date_str2)
leap_years = leap_years_between_dates(date_str1, date_str2)

print("Seconds between the two dates:", seconds)
print("Number of leap years between the two dates:", leap_years)

for date_str in [date_str1, date_str2]:
    dst = daylight_savings_time(date_str)
    jalali_date = convert_to_jalali(date_str)
    print("{}: Daylight Savings Time: {}, Jalali Date: {}".format(date_str, dst, jalali_date))
