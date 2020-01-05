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
squares = [value**2 for value in range(1,11)]
print(squares)
#
numbers = [val for val in range(1, 11)]
print(numbers)
#
nums = []
for value in range(1, 101):
    nums.append(value)

print(nums)
#
my_list = [1, 2, 3]
friend_list = my_list[:]#копируется список только срезом, иначе получится клон
#
dimensions = (200, 50)#кортеж в круглых скобках(не изменяется), но можно переопределиь весь кортеж в вызове
print(dimensions[0])
print(dimensions[1])
####################
#Глава 5: команды if
####################
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
#################
#Глава 6: словари
#################
alien_0 = {'color': 'green', 'points': 5}#инициализация словаря
print(alien_0['color'])
print(alien_0['points'])
#
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print alien_0
#
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
#
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():#обращение key только по ключу словаря, value только по значению, items и по ключу и по значению
    print("\nKey: " + key)
    print("Value: " + value)
#
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + \
        language.title() + ".")
#
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:#по умолчанию имеется в виду всегда имя
    print(name.title())
#
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + \
            favorite_languages[name].title() + "!")
#
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):#set проверяет повторы в множестве и выводит только уникальные имена
    print(language.title())
#
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))
#
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print("You ordered a " + pizza['crust'] + "-crust pizza " + \
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
###Глава 7: ввод данных и циклы###
#
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue#игнорирует оставшийся код цикла и запускает некст проход (break прерывает цикл полностью)
    print(current_number)
#
unconfirmed_users = ['alice', 'brian', 'candace']
unconfirmed_users = sorted(unconfirmed_users, reverse=True)#реверс для красоты вывода, т.к. pop режет список с конца
confirmed_users = []
while unconfirmed_users:#пока есть элементы = True
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)
#
responses = {}

polling_active = True
while polling_active:
    name = 'name'
    response = 'everest'
    responses[name] = response#представление словаря
    repeat = 'no'
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
###Глава 8: функции###
#
def greet_user():
    print('Hello World!')

greet_user()
#
def describe_pet(pet_name, animal_type='dog'):#использование параметра по умолчанию
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')#явное указание имени (можно и не явно т.к. первый аргумент это имя)
#
def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#
def get_formatted_name(first_name, last_name, middle_name=''):#среднее_имя по умолчанию пусто и игнорируется функцией как значение (bool = False)
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
#
def build_person(first_name, last_name):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
#
def build_person(first_name, last_name, age=''):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
#
def greet_users(names):
    """Вывод простого приветствия для каждого пользователя в списке."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
#
def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Имитация печати модели на 3D-принтере.
        print("Printing model: " + current_design)
        completed_models.append(current_design)#список сохраняется и для внешней переменной вне функции

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
#
def make_pizza(size, *toppings):#* позволяет передавать в аргумент кортеж неопределённого размера
    """Выводит описание пиццы."""
    print("\nMaking a " + str(size) + \
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
def build_profile(first, last, **user_info):#** передаёт в аргумент словарь произвольного размера
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', \
    location='princeton', field='physics')
print(user_profile)
#import имя - функции модуля писать через имя.имя_модуля
#from имя import функция (или * если импорт всего) - функция сохраняет своё имя и пишется без .
#import имя as другое_имя - присваивание псевдонима
###Глава 9: классы###
class Dog():
    """Простая модель собаки."""
    def __init__(self, name, age):#главная функция, зарезервированные символы __, является частью класса и исполняется автоматически
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age
    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('Willie', 8)#стандартная не явная инициализация объекта класса
print("My dog's name is " + my_dog.name.title() + ".")#обращение к атрибутам класса через имя_объекта.имя_атрибута (если класс определн через self)
print("My dog is " + str(my_dog.age) + " years old.")#str потому что в вызове класса передано число а не символ
#
