def season(num):
    if num >= 1 and num <= 12:
        if num <=2 or num >=12 :
            print('зима')
        elif num <= 5:
            print('весна')
        elif num <= 8:
            print('лето')
        else:
            print('осень')
            
num_of_season = int(input('Введи число месяца: '))
season(num_of_season)