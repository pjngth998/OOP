def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



def day_of_year(day, month, year):
    day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
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

def date_diff(date1,date2):
    diff = 0
    try:
        date1 = date1.strip().split("-")
        date2 = date2.strip().split("-")
        day1, month1, year1 = [int(x) for x in date1]
        day2, month2, year2 = [int(x) for x in date2]
        day1st = day_of_year(day1, month1, year1)
        day2nd = day_of_year(day2, month2, year2)
        if year1 > year2 :
            raise Exception
        if date1 == date2:
            return 1
        if year1 == year2 :
            if day1st > day2nd:
                raise Exception
            else :
                return day2nd - day1st + 1
        
        for i in range(year1,year2):
            if i == year1:
                diff = (365 + is_leap(year1)) - (day_of_year(day1, month1, year1))
            else:
                if is_leap(i):
                    diff += 366
                else:
                    diff += 365
            
        diff += day_of_year(day2, month2, year2)
        return diff + 1
    except:
        return "Invalid"
try:
    date1, date2 = input("Enter Input: ").strip().split(", ")
    
    print(date_diff(date1, date2))
    
except:
    print("Invalid")

