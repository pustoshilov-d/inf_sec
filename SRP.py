import random

from HashFunction import hash1, hash2
from SimpleNum import generateSimple, isSimple

def global_print(*names) -> None:
    # x = lambda s: ["{}", "0x{:x}"] [hasattr(s, 'real')].format(s)
    print("".join("{} = {}\n".format(name, globals()[name]) for name in names))

#known by both sides
n_bit = 15
n_bit_small = 6
q = generateSimple(n_bit)
N = 2*q + 1 #modulo
while not(isSimple(N)):
    q = generateSimple(n_bit)
    N = 2 * q + 1

print('\n')
k = 3 #as for 6 version
H = hash1 #hash-function
g = generateSimple(n_bit_small) #generator
global_print("H", "N", "g", "k")



#server
I = 'Dmitry' #name
p = 'passsword' #password
s = random.randint(0,pow(2,n_bit_small)) #salt
x = H(s,p, n_bit = n_bit_small)
v = pow(g,x)
server_base = [I,s,v]
global_print("I", "p", "s", "x", "v")
global_print("server_base")

#athentication
#client identification
a = random.randint(0,pow(2,n_bit_small))
A = pow(g,a)
#sending A, I
global_print("A", "I")

#server
b = random.randint(0,pow(2,n_bit_small))
B = k*v + pow(g,b)
#sending s, B
global_print("B", "s")


#both sides
u = u_C = u_S = H(A,B, n_bit = n_bit_small)
global_print("u")

#client
#password entering
x = H(s,p, n_bit = n_bit_small)
#key of session
S_c = pow(B - k*pow(g,x), a + u_C*x)
#encrypting key
K_c = H(S_c, n_bit = n_bit_small)
global_print("S_c", "K_c")

#server
#key of session
S_s = pow(A * pow(v,u_S),b)
#encrypting key
K_s = H(S_s, n_bit = n_bit_small)
global_print("S_s", "K_s")

global_print("K_c", "K_s")

#client
M_c = H(H(N,n_bit = n_bit_small) ^ H(g,n_bit = n_bit_small),
        H(I,n_bit = n_bit_small), s, A, B, K_c,n_bit = n_bit_small)
global_print("M_c")
#sending M_c to proof session key

#server
M_s = H(A, M_c, K_s,n_bit = n_bit_small)
global_print("M_s")
#sending M_s to proof session key