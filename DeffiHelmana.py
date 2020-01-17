# -*- coding: utf8 -*-
import random
def pervoobraz(g,p):
    data = set()
    for i in range(p):
        data.add(pow(g, i, p))
    return len(data) == p - 1




#публичные простой модуль и генератор
common_g = 	3
# common_p = random.randint(1,1000)
common_p = 17

print(pervoobraz(common_g,common_p))

print("Алиса и Боб публично определяют модуль и генератор")
print(common_g, common_p)

Alice_private = random.randint(1,1000)
Alice_sending = pow(common_g, Alice_private, common_p)
print("Алиса посылает Бобу: ", Alice_sending)

Bob_private = random.randint(1,1000)
Bob_sending = pow(common_g, Bob_private, common_p)
print("Боб посылает Алисе: ", Bob_sending)

Alice_common = pow(Bob_sending, Alice_private, common_p)
Bob_common = pow(Alice_sending, Bob_private, common_p)
print(Alice_common, Bob_common, Alice_common == Bob_common)