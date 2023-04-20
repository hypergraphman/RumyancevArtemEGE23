from itertools import permutations

set_word = set()
# list_word = []
for w in permutations('MAMA'):
    word = ''.join(w)
    if 'MM' not in word and 'AA' not in word:
        # print(word)
        # list_word.append(word)
        set_word.add(word)
print('----------')
print(*set_word, sep='\n')