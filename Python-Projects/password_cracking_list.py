from string import *
from itertools import product

value = ascii_letters + digits + punctuation

for i in range(0,5):
    for j in product(value, repeat=i):
        word = '' .join(j)
        p = open('password.txt', "a")
        p.write(word)
        p.write('\n')

