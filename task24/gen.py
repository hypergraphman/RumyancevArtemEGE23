from random import choice
from string import ascii_uppercase

with open('24-r7.txt', 'w') as f:
    for i in range(10**6):
        f.write(choice(ascii_uppercase))
