for a in range(0, 10000):
    is_a = True
    for x in range(0, 10000):
        if not ((x & 85 == 0) <= ((x & 54 != 0) <= (x & a != 0))):
            is_a = False
            break
    if is_a:
        print(a)
        break


for a in range(0, 10000):
    if all((x & 85 == 0) <= ((x & 54 != 0) <= (x & a != 0)) for x in range(0, 10000)):
        print(a)
        break