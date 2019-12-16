num = int(input())

if num % 2 == 0:
    less_per = num/2
    max_per = num/2 - 1
else:
    less_per = (num-1)/2
    max_per = (num-1)/2

num_ex = 45*num + 5*less_per + 15*max_per

print(less_per, max_per, num_ex)

min = int(num_ex % 60)
hour = int(9 + (num_ex - min) / 60)

if min<10:
    min = '0'+ str(min)