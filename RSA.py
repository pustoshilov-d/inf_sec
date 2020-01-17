# -*- coding: utf8 -*-
from SimpleNum import generateSimple
# import gmpy2

def generateSemiSimple(a):
    i = 3
    while True:
        flag = True
        for j in range(2, i+1):
            if a % j == 0 and i % j == 0:
                flag = False
                break
        if flag: return i
        else: i += 2


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    # print(g, x, _)
    if g == 1:
        return x % n

n_bit = 10

p = generateSimple(n_bit)
q = generateSimple(n_bit)
# p = 3557
# q = 2579
n = p * q
f = (p-1)*(q-1)
e = generateSemiSimple(f)

d = mulinv(e,f)
print(e,n, ' public')
print(d,n,' secret')

#фишрование
Message = 111111
print(Message)
Encrypted = pow(Message, e, n)
print(Encrypted)
Decrypted = pow(Encrypted, d, n)
print(Decrypted)
