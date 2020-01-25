# This code is taken from Alex Martinelli
# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-in-any-base-to-a-string/2267446#2267446

import string
digs = string.digits + string.ascii_letters

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

print("15 in hex: " + int2base(15, 16))
print("255 in hex: " + int2base(255, 16))
print("64 in hex: " + int2base(64, 16))
