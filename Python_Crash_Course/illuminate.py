### ИМПОРТ ВСЕХ РАБОЧИХ ЛИБ И ФУНКЦИЙ ###
import pygame # Игровая либа
import random

### КОНСТАНТЫ ###
# Инициализация констант цвета RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVY_BLUE = (0, 0, 128)
OLIVA = (128, 128, 0)
PURPLE = (128, 0, 128)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
# Стандартные разрешения окна в пикселях
low_res = (800, 600)
hd_res = (1024, 720)
full_hd_res = (1920, 1080)
# Размеры pyxel:
small_py = 10
middle_py = 25
big_py = 50

### НАСТРОЙКИ ###
# Настройки (экран, отображение, всё что меняется извне)
background_color = WHITE # Цвет фона из Const
window_resolution = low_res # Разрешение из стандартных
window_name = 'DEFAULT' # Имя окна
fps = 60 # Установка количества итераций отрисовки главного экрана в секунду

### УСТАНОВКА ПАРАМЕТРОВ ПЕРЕД ГЛАВНЫМ ЦИКЛОМ ###
# Инициализация движка
pygame.init()
pygame.mixer.init()# Для звука

# Подключение функций библиотеки Pygame
main_screen = pygame.display.set_mode(window_resolution) # Инициализация переменной screen как главной рабочей области, привязка размера окна из Const
pygame.display.set_caption(window_name) # Наименование в шапке окна

# Классы, объекты и переменные:
class Pyxel():

    def __init__(self, x, y, color = WHITE, size = middle_py):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

pyxel_pull_x = [x for x in range(0, window_resolution[0], pyxel.size)]
pyxel_pull_y = [y for y in range(0, window_resolution[1], pyxel.size)]
pyxel_pull = []

for x in pyxel_pull_x:
    for y in pyxel_pull_y:
            pyxel_pull.append(x)
            pyxel_pull.append(y)

for pyxel_x in pyxel_pull in range(0, pyxel_pull[-1], 2):
    for pyxel_y in pyxel_pull in range(1, pyxel_pull[-1], 2):
        pyxel = Pyxel(pyxel_x, pyxel_y)

#print(pyxel_pull)

# Инициализация флагов
exit_game = False # Флаг главной петли, работает пока не будет нажата кнопка закрытия окна

# Инициализация переменной tick_rate, количество тиков в секунду (фпс)
tick_rate = pygame.time.Clock()

### ГЛАВНЫЙ ЦИКЛ ###
# Главная петля, логически то же самое что и while done == False (пока не нажат крестик окна)
while not exit_game:
    # Управляет fps, или количеством итераций главного цикла за секунду
    # Оставь значение в скобках пустым и программа будет использовать весь ЦП который будет доступен
    tick_rate.tick(fps)
    # Запуск цикла pygame для регистрации input устройств
    for event in pygame.event.get():  # Когда юзер что-то делает
        if event.type == pygame.QUIT:  # Когда нажимает крестик
            exit_game = True  # Флаг close_button становится True, следовательно следующий цикл не начнётся
            break

    # Очистка окна и отрисовка фона
    main_screen.fill(background_color)
    
    # Игровая логика
    
    # Здесь отрисовываем наши объекты

    # Update окна в конце отрисовки логики
    # Данная команда ОБЯЗАНА выполняться после всех команд логики и отрисовки, иначе изменения не отобразятся
    pygame.display.flip()

### КОНЕЦ ПРОГРАММЫ ###
# После выполнения цикла, когда close_button = True (был нажат крестик), закрыть модуль Pygame, следовательно  закрыть окно и всю пограмму
pygame.quit()