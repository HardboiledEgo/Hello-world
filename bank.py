def bank(a, proc, years):
    res = 0
    i = 0
    while i < years:
        res = a + 0.01 * proc * a
        a = res
        i += 1
    return(res)

a = int(input('Введи сумму в банке: '))
proc = int(input('Введи процент вклада: '))
years = int(input('Введи срок вклада в годах: '))
print(bank(a, proc, years))