from itertools import permutations

al = 'KAPKAN'
res = set()
for word in permutations(al):
    word = ''.join(word)
    if 'KK' not in word and 'AA' not in word:
        res.add(word)
print(len(res))