n, *a = map(int, open('27_B.txt').read().split())
k = 157
# print(n, a)
# min_len = 10**10
max_sum = 0
# better_index_prefix_sum = [0] * k
b = [0] * k
prefix_sum = [0]
ln = 10**10
for i in range(n):

    s = prefix_sum[-1] + a[i]
    t = s % k
    if t == 0 or b[t] != 0:
        if s - prefix_sum[b[t]] > max_sum:
            max_sum = s - prefix_sum[b[t]]
            ln = i - b[t] + 1
        elif s - prefix_sum[b[t]] == max_sum:
            ln = i - b[t] + 1
    prefix_sum.append(s)
    if t != 0 and b[t] == 0:
        b[t] = i + 1
    if ln == 1497991:
        print(ln)
print(ln, max_sum)