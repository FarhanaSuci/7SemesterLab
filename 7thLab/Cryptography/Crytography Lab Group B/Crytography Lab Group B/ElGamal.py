import math, random
from sympy import primitive_root,randprime

def keyGeneration():
    #Step1: Select a large prime number p
    p = int(input(f"Enter a large prime number p: "))
    #Step2: Select d to be a member of the group G = <Zp*, *> such that 1 <= d <= p-2
    d = random.randint(1, p-2)
    # d = 3
    print(f"Private Key: {d}")
    #Step3: Select e1 to be the primitive root in the group G = <Zp*, *>
    # e1 = 2
    # The number for which you want to find the primitive root
    # p = randprime(124, 10 ** 3)
    e1 = primitive_root(p)
    print(f"One of the Primitive root of {p} is: {e1}")

    #Step4: e2 = e1^d mod p
    e2 = mod_power(e1, d, p)
    print(f"Public Key: {e1},{e2},{p}")
    return e1, e2, p, d

def mod_power(a, n, m):
    r = 1  #r is the output value or return value
    # y = a % m , here y is y0, since it will be done anyway in line 84, we omit this line And since y is not used any further, we can replace yi with a
    while n > 0:
        if n & 1 == 1:  #Here, we grab every bit b0, b1, b1,..,bt and move them to the LSB position, when bitwise ANDED with ...0001, All the bits except the LSB bit is 0ed,
            # only the LSB bit is preserved.
            #Then we right shift the n by 1 (line 85) so that the next bit position b1 comes to the LSB position, in this way we traverse the binary digits in reverse order(from b0 to bt), we do this until all the bit values becomes 0 in which case bi becomes 0 and we break out of the while loop
            r = (r * a) % m #Same as product of yi(mod m) if the corresponding bit value is 1
        a = (a * a) % m #same as yi + 1 = (yi)^2 the recurrence relation we established on slide, it needs to be done for every bit position no matter what(bi can be 0 or 1)
        n >>= 1 #Every time, I advance the bit position further
    return r



def encrypt(e1, e2, p, msg):
    #Step1: Select a random integer r in the group G = <Zp*, *>
    r = random.randint(1, p-1)
    # r = 4
    #c1 = e1^r mod p
    c1 = mod_power(e1, r, p)
    #c2 = (msg * e2^r) mod p = (msg mod p) * (e2^r mod p)
    c2 = (msg % p) * mod_power(e2, r, p)
    return c1, c2


def decrypt(d, p, c1, c2):
    #msg = (c2*(c1^d)^(-1)) mod p
    res = pow(c1 ** d, -1, p)
    P = (c2 * res) % p
    return P


def main():
    msg = int(input(f"Enter the message(in numerical value): "))
    print(f'Original message:{msg}')
    # This routine creates the public and private key at the receiver side
    e1, e2, p, d = keyGeneration()
    c1, c2 = encrypt(e1,e2,p,msg)
    print(f'Encrypted message: ({c1},{c2})')
    decryptedPlainText = decrypt(d, p, c1, c2)
    print(f'Decrypted message: {decryptedPlainText}')

if __name__ == '__main__':
    main()