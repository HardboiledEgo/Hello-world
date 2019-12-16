from math import sqrt

def square(a):
    p = 4 * a
    s = a ** 2
    d = sqrt(2) * a
    res = (p, s, d)
    return(res)

a = int(input('Введите сторону квадрата: '))
print(square(a))