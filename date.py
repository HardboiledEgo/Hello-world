def date(day, month, year):
    third_one_day_month_list = (1, 3, 5, 7, 8, 10 ,12)
    third_day_month_list = (4, 6, 9, 11)
    if year >= 1:
        if month >= 1 and month <= 12:
            if day>=1 and day <= 28:
                return True
            elif day == 31 and month in third_one_day_month_list:
                return True
            elif day == 30 and month in third_day_month_list:
                return True
            elif day == 29 and month == 2 and ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0)):
                return True
            else:
                return False
        else:
                return False
    else:
                return False

year = int(input('Введи год: '))
month = int(input('Введи месяц: '))
day = int(input('Введи день: '))
print(date(day, month, year))