# -*- coding: utf8 -*-
import random
import numpy as np

def Rabin_test(p):
    b = 0
    p_new = p - 1
    while True:
        if p_new % 2 == 0:
            b += 1
            p_new //= 2
        else: break
    # print("p = ", p)
    # print("b = ", b)
    m = (p-1) // pow(2,b)
    # print("m = ", m)

    a = random.randint(1,p)
    z = pow(a,m,p)
    if z == 1 or z == p-1:
        return True

    for j in range(b):

        z = pow(z, 2, p)

        if z == 1:
            return False
        if z == p - 1:
            return True

    return False

def Eratosphen(n):
    list = [i for i in range(2,n+1)]

    flag = True

    p = list[0]

    while flag:
        k = p*2
        while k <= n:
            try:
                list.remove(k)
            except: pass
            k += p
        p_last = p
        for i in list:
            if i > p:
                p = i
                break
        flag = p_last != p
    return list

def Erat_test(p,simple):
    flag = True
    for i in simple:
        if p != i and p % i == 0:
            flag = False
            break
    return flag

def generateSimple(n_bit):
    simple2000 = Eratosphen(2000)
    mask = list("0" * n_bit)
    mask[0] = "1"
    mask[-1] = "1"
    mask = int("".join(mask),2)

    flag = True
    while flag:
        random_p = random.randint(pow(2,n_bit-1),pow(2,n_bit)-1)

        random_p = random_p | mask
        print(random_p)

        if not(Erat_test(random_p,simple2000)):
            print('Erat test fail')
            continue
        else: print('Erat test passed')

        test_flag = True
        for i in range(5):
            if not(Rabin_test(random_p)):
                print('Rabin test fail')
                test_flag = False
                break
            else: print('Rabin test passed')

        if test_flag:
            print('Thats is simple')
            flag = False
            return random_p

print(generateSimple(100))