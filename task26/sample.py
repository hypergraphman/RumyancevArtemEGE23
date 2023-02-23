a = [3, 54, 2, 65, 12, 6, 2]
a.sort(key=lambda x: sum(map(int, str(x))))
print(a)