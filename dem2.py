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

for i in range(1, len(directories)):
    sheet.