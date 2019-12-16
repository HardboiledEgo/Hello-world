def is_prime(num):
    if num == 0 or num == 1:
        return('Число ' + str(num) + ' является ни простым ни составным числом')
    if num % 2 != 0 or num == 2:
        return('Число '+ str(num) +' простое')
    else:
        return('Число '+ str(num) +' сложное')
        
num = int(input('Введите число: '))
print(is_prime(num))