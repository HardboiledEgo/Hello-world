#Глава 1 представляет собой установку Питона и IDE
##########################################
#Глава 2: Переменные и простые типы данных
##########################################
print('Hello World!')#печатает сообщение
#
name = 'ada lovelace'#переменная
print(name.title())#печать переменной с методом: первый символ - заглавный, остальные маленькие
#
name = 'Ada Lovelace'
print(name.upper())#другой метод печати: все верхние
print(name.lower())#метод печати: все нижние
#
first_name = 'ada'
second_name = 'lovelace'
full_name = first_name + ' ' + second_name#конкатенация (сложение) символов в переменную
print('Hello,' + ' ' + full_name.title() + '!')#конкатенация прямо в печати символов и значения переменной
#
print('\tPython')#таб(\t)
print('1\n2\n3\n4\n5')#энтер(\n)
print('Languages:\n\tC++\n\tPython\n\tJava')
#
message = 'words '
message#>>>(вызов в терминале) вернёт 'words '
message.rstrip()#метод rstrip обрежет пробел справа и вернёт 'words'
#
message = ' words '
message.lstrip()#>>> метод обрежет пробелы слева
message.strip()#>>> метод обрежет все пробелы
message = message.strip()#можно перезаписывать значение переменной методом "на лету"
#
2**3 = 8#двойной знак умножения означает возведение в степень
0.2 + 0.1 = 0.3#вернёт 0.30...04, чаще всего всё считает правильно но из-за маленьких чисел сложение "просто так в терминале" вызывает косяки интерпретатора, пока не важная деталь но после объяснят как делать правильно
#
age = str(23)
print('Happy ' + age + '"rd birthday!')#кавычки внутри ковычек следует ставить не те, что использовались внтури print для обозначения внтуреннего сообщения. можно использовать либо ' либо ", но внутри использовать другую пару. для обозначения символов, а не числа, обозначаем для вывода 23 как str(), то есть строку. иначе выпадет ошибка несовместимости типов, когда в строку пытаемся сложить число.
#либо
age = 23
print('Happy ' + str(age) + '"rd birthday!')
#
#УПРАЖНЕНИЯ
###############
#Глава3: Списки
###############
bicycles = ['trek', 'cannondale', 'redline', 'specialized']#инициализация списка
print(bicycles[0])#нумерация в списках начинается с 0, следоавтельно обращение к первому элементу по индексу 0
print(bicycles[0].title())#для вывода строковых значений можно применять форматирование из главы 2
print(bicycles[-1])#для удобства всегда последний элемент списка будет вызываться по индексу -1(то же справедливо и для -2(предпоследний элемент) и т.д.)
#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = 'Shrek'#замена первого значения списка
print(bicycles)
#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('honda')#добавление значения в конец списка
print(bicycles)
#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(0, 'ducati')#добавляет элемент списка в указанный индекс
print(bicycles)
#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[0]#удаляет указаный по индексу элемент
print(bicycles)
#
moto = ['honda', 'suzuki', 'yamaha']
popped_moto = moto.pop()#"вырезает" из списка последний элемент и присваивает переменной
print(moto)
print(popped_moto)
#
moto = ['honda', 'suzuki', 'yamaha']
popped_moto = moto.pop(0)#"вырезает" из списка указанный(в данном случае первый) элемент и присваивает переменной
print(moto)
print(popped_moto)
#
moto = ['honda', 'suzuki', 'yamaha']
moto.remove('yamaha')#удаляет из списка указанный элемент по значению
print(moto)
#
moto = ['honda', 'yamaha', 'suzuki', 'yamaha']
too_expensive = 'yamaha'
moto.remove(too_expensive)#удаляет из списка первый элемент совпадающий с значением переменной
print(moto)
#
#УПРАЖНЕНИЯ
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()#сортировка списка (по умолчанию в алфавитном порядке)
print(cars)
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)#сортировка списка (в указанном обратном порядке)
print(cars)
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))#временная сортировка списка печати
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))#временная сортировка списка печати
print(sorted(cars, reverse=True))#(сортировка в обратном порядке)
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()#присваивает переменной обратный список
print(cars)
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))#длина списка
#
#УПРАЖНЕНИЯ
############################
#Глава 4: работа со списками
############################
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#
for value in range(1,6):
    print(value)
#
numbers = list(range(1,6))
print(numbers)
#
numbers = list(range(2,11,2))#с увеличение на 2
print(numbers)
#
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
min(digits)
max(digits)
sum(digits)
#
squares = [value**2 for value in range(1,11)]
print(squares)
#
nums = [nums.insert(0, value) for value in range(1, 11)]
print(nums)
#
nums = []
for value in range(1, 101):
    nums.append(value)

print(nums)
#
my_list = [1, 2, 3]
friend_list = my_list[:]#копируется список только срезом, иначе получится клон
#
