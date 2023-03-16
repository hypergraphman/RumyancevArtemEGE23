# Сколько 5 значных чисел в 8й сс, в которых есть
# 2 четверки и рядом сними только четные числа
from itertools import product


def check_even(word):
    for i in range(len(word)):
        if word[i] == '4':
            if i == 0:
                if word[i + 1] not in '0246':
                    return False
            elif i == len(word) - 1:
                if word[i - 1] not in '0246':
                    return False
            else:
                if word[i + 1] not in '0246' or word[i - 1] not in '0246':
                    return False
    return True


al = '01234567'
res = set()
for word in product(al, repeat=5):
    word = ''.join(word)
    if word[0] != '0' and word.count('4') == 2 and check_even(word):
        res.add(word)
print(len(res))