zaka = [[-6, -1, -1, 2], [-1, -8, -1, -5], [-1, -8, -8, -8], [2, -8, -4, 0]]
for i in zaka :
    print(*map("{:2d}".format, i))
n = 2
zaka_rev = list(map(list,zip(*zaka)))
for i in range(n) :
    for j in range(n) :
        if zaka[i] == zaka_rev[j] :
            print(i+1, "строка и", j+1, "столбец равны")