f = open('26.txt')
v, n = map(int, f.readline().split())
a = [int(x) for x in f.readlines()]
f.close()

a.sort()
k = 0
while v - a[k] >= 0:
    v -= a[k]
    k += 1
print(k, v)
v += a[k - 1]

# mx = 0
# for el in a[k-1:]:
#     if mx < el <= v:
#         mx = el
# print(mx)

print(max(filter(lambda x: x <= v, a)))
