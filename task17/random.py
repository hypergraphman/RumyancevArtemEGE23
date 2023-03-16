from collections import Counter

with open('17-332.txt') as f:
    a = list(map(int, f.readlines()))

avg17 = 0
s = 0
k = 0
for el in a:
    if el % 17:
        s += el
        k += 1
avg17 = s / k

res = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if sum(map(int, str(p1))) == sum(map(int, str(p3))) and p2 < avg17:
        res.append(sum(map(int, str(p2))))

print(len(res))
print(Counter(res))