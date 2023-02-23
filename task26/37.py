f = open('26-k6.txt')
n, k = map(int, f.readline().split())
d = []
for line in f.readlines():
    w, p = map(int, line.split())
    d.append((p / w, w))

d.sort(key=lambda x: (x[0], -x[1]))

# print(*d, sep='\n')
s = 0
mx = d[0]
for cost, weight in d[:k]:
    s += weight
    if weight > mx[1]:
        mx = (cost, weight)
print(s, mx[0] * mx[1])
