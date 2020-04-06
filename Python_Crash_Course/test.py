low_res = (800, 600)

window_resolution = low_res # Разрешение из стандартных

pyxel_pull_x = [x for x in range(0, window_resolution[0], 50)]
pyxel_pull_y = [y for y in range(0, window_resolution[1], 50)]
pyxel_pull = []

for x in pyxel_pull_x:
    for y in pyxel_pull_y:
            pyxel_pull.append(x)
            pyxel_pull.append(y)


print(pyxel_pull)

