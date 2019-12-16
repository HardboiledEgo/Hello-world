def is_year_leap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0)):
        return('\nГод високосный! :)')
    else:
        return('\nГод не високосный :(')
    
print(is_year_leap(2000))
        
