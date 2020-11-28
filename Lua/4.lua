io.write('5+3=', 5+3, '\n')
io.write('5-3=', 5-3,'\n')
io.write('5*3=', 5*3, '\n')
io.write('5/3=', 5/3,'\n')
io.write('5.2%3=', 5.2%3, '\n')
io.write('5.2//3=', 5.2//3, '\n')

--[[получение одинакого ключа для псевдослучайных чисел. считается, что рандом отрабатывает лучше на одном и том же сиде, все последующие числа к нему привязаны]]

math.randomseed(os.time())

io.write('math.random() ', math.random(), '\n')
io.write('math.random(10) ', math.random(10), '\n')
io.write('math.random(20,30) ', math.random(20,30), '\n')

print(string.format('Pi = %.2f', math.pi)) 

--[[знак % привязаывает переменную в вызове к math.pi]]