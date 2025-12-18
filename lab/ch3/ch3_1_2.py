def is_leap(year):
    try:
        year = int(year)
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    except:
        return "False"

day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def day_of_year(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        day_of_year = 0
        if month > 12 or month < 1:
            raise Exception
        if is_leap(year):
            day_in_month[2] += 1
        else:
            if month == 2 and day == 29:
                return -1
        for i in range(1,month):
            day_of_year += day_in_month[i]
        day_of_year += day
        return day_of_year
    except:
        return "Invalid"

try:
    ip = input("Enter a date : ").strip().split("-")
    day, month, year = ip
    print("day of year: {} ,".format(day_of_year(day,month,year)),end="")
    print("is_leap: {}".format(is_leap(year)))
except:
    print("day of year: Invalid ,is_leap: False")
# except:
#     if ip[2].isdigit() == True and int(ip[2]) > -1:
#         print("day of year: Invalid ,",end="")
#         print("is_leap: {}".format(is_leap(int(ip[2]))))
#     else:
#         print("day of year: Invalid ,is_leap: False")

