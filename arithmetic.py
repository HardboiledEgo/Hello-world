def arithmetic(x, y, op):
    if op == '+':
        sum = x + y
    if op == '-':
        sum = x - y
    if op == '*':
        sum = x*y
    if op == '/' or op == ':':
        sum = x/y
    return(sum)


print(arithmetic(25, 10, ':'))
    