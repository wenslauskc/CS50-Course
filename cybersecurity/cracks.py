from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters + punctuaton + digits, repeat = 8):
    print(*passcode)