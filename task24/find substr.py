with open('24-r7.txt') as f:
    s = f.read()

max_len = 1
cur_len = 1
i_last_max_len = 0
for i in range(1, len(s)):
    c1, c2 = s[i - 1], s[i]
    if c1 != c2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            i_last_max_len = i
    else:
        cur_len = 1
print(s[i_last_max_len - max_len + 1: i_last_max_len + 1])