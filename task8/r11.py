from itertools import product

al = 'SKOLA'
res = set()
for word in product(al, repeat=3):
    word = ''.join(word)
    if word.count('K') == 1:
        res.add(word)
print(len(res))
