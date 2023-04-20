n, *a = map(int, open('27_A.txt').read().split())
k = 157
# print(n, a)
# min_len = 10**10
max_sum = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s % k == 0:
            if s > max_sum:
                max_sum = s
                min_len = j - i + 1
            elif s == max_sum and j - i + 1 < min_len:
                min_len = j - i + 1
print(min_len, max_sum)