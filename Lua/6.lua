--[[i = 1
while (i <= 15) do
  io.write(i, "\n")
  i = i + 1
  if i == 8 then break end
end]]

--[[repeat 
  io.write("Enetr your guess ")
  guess = io.read()
until tonumber(guess) == 15]]

for i = 1, 10, 1 do
  io.write(i, '\n')
end

months = {'Jan', 'Feb', 'Mart', 'Apr', 'May', 'Jun', 'Jul'}
for keys, value in pairs(months) do
  io.write(value, " ")
end