print('x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int((w == (z <= x)) and y)
                print(x, y, z, w, f)