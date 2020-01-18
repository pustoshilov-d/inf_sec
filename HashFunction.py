from SimpleNum import generateSimple

def hashForAll(*args, n_bit = 30):
    res = ''
    for A in args:
        res += "".join([str(ord(i)) for i in str(A)])
    batch = (n_bit // 3) + 1
    D = [int(res[i:i+batch]) for i in range(0, len(res), batch)]
    E = int("1"*batch)
    for i in D:
        E = E ^ i
    F = E % pow(2, n_bit-1) + pow(2, n_bit) - 1
    return F

def hashForNumbers(*args, n_bit = 30):
    import math
    h = 0x811c9dc5
    if n_bit > 10:
        str_ = list("0" * n_bit)
        str_[0] = '1'
        delta = int("".join(str_),2) + 403
    else:
        delta = 403

    B = "".join(str(i) for i in args)
    for i in B:
        h = (h ^ int(i)) * delta
    print(h)
    F = h % pow(2, n_bit-1) + pow(2, n_bit) - 1
    return F


def hashExperimental(*args, modulo = 547273483, n_bit=30):
    import math
    res = 0
    for A in args:
        res += int("".join([str(ord(i)) for i in str(A)]))
    res = str(int(res) + modulo)
    h = 0
    for i in range(len(res)):
        h += int(res[i]) * math.exp(i)

    F = pow(3, int(h), modulo) + pow(2, n_bit) - 1
    # print(F)
    return F

if __name__ == '__main__':

    # print(hash1(123452124322222878823, 1234521325325326326236236436223))
    print(hashForNumbers(123452124322222878823, 1234521325325326326236236436223))
    print(hashForAll('passswored', 'dweqd231dew', '31ddwd22'))
    # H = hashForNumbers
    H = hashForAll
    # H = hashExperimental
    print(H('passswored', 'dweqd231dew', '31ddwd22'))
    max = 10000
    flag = False
    N = generateSimple(30)
    print(N)
    for i in range(max):
            print(i)
            for j in range(max):
                # print(H(j))

                #необратимость
                if i != j:
                    if H(j) == i:
                        print(i, j)
                        print("Необратимость нарушена")
                        flag = True
                    #коллизии 1 уровня
                    if H(i) == j:
                        print(i, j)
                        print("Коллизия 1")
                        flag = True
                    #коллизии 2
                    if H(i) == H(j):
                        print(i, j)
                        print("Коллизия 2")
                        flag = True
                if flag: break
            if flag: break

    print(H(2), H(1))
