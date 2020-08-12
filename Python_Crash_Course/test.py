import math
num_input = int(input('введи десятичное число: '))
tenet = int(input('введи необходимое основание: '))
num_output = []
while num_input > 1:
    num_output.append(num_input % tenet)
    if num_input == tenet:
        num_output.append(1)
        break
    else:
        num_input = num_input // tenet
num_output.reverse()
print(num_output)
input('***')