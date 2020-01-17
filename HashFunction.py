def hash1(*args, n_bit = 400):
    n_max = pow(2, n_bit)
    res = 0
    for A in args:
        res += int("".join([str(ord(i)) for i in str(A)]))
    return res % n_max

def hash2(A):
    import math
    n_max = pow(2, 500)
    res = [math.sin(int(i))+math.cos(int(i)) for i in str(A)]
    sum = 0
    for i in res:
        sum += i

    return round(n_max - int(sum))

print(hash1(123452124322222878823, 1234521325325326326236236436223))
print(hash2(1234521325325326326236236436223))
print(hash1('3213de', '2dewq'))
# for i in range()
