
#Подключаем модуль
import os
import openpyxl

#Каталог из которого будем брать изображения
directory = 'C:/Users/kirill.poltavetc/Downloads/Для WB'
wb = openpyxl.Workbook()

# добавляем новый лист
wb.create_sheet(title = 'Лист 1', index = 0)

# получаем лист, с которым будем работать
sheet = wb['Лист 1']
filenames = ''

#Получаем список файлов в переменную files
directories = os.listdir(directory)

for direct in directories:

    filename = os.listdir(directory+'/'+direct) 

    dirs = ('папка: '+ direct)
    dirs_l = list(dirs)
    print(dirs)
    sheet.append(dirs_l)

    filenames = ('файлы: '+str(filename))
    filenames_l = list(filenames)
    print(filenames)
    sheet.append(filenames_l)

wb.save('example.xlsx')