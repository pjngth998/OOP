def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def day_of_year(day, month, year):
    day_of_year = 0
    try:
        if month > 12 or month < 1:
            raise Exception
        if is_leap(year):
            day_in_month[2] += 1
        else:
            if month == 2 and day >= 29:
                raise Exception
        if day < 1 or day > day_in_month[month]:
            raise Exception
        for i in range(1,month):
            day_of_year += day_in_month[i]
        day_of_year += day
        return day_of_year
    except:
        return "Invalid"

try:
    ip = input("Enter a date : ").strip().split("-")
    day, month, year = [int(x) for x in ip]
    print("day of year: {} ,".format(day_of_year(day,month,year)),end="")
    print("is_leap: {}".format(is_leap(year)))
except:
    if ip[2].isdigit() == True and int(ip[2]) > -1:
        print("day of year: Invalid ,",end="")
        print("is_leap: {}".format(is_leap(int(ip[2]))))
    else:
        print("day of year: Invalid ,is_leap: False")

