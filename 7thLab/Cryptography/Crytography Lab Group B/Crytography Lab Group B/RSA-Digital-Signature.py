import math, random

def keyGeneration():
    #Step 1 --> Select two large prime numbers such that p != q
    p = int(input(f"Enter first large prime number p: "))
    while True:
        q = int(input(f"Enter second large prime number q: "))
        if q == p: 
            print(f"Please select a different prime number other than {p}")
        else:
            break
    
    
    # step 2 --> Calculate n = p * q
    n = p * q
    print("n =", n)

    # step 3 --> calculate phi(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # step 4 --> select an integer e such that 1 < e < phi(n) and e is coprime to phi(n)
    while True:
        e = random.randint(2, phi-1)
        print(f"The random integer e: {e}")
        # checking whether e is coprime to phi(n)
        if (math.gcd(e, phi) == 1):
            break
        else:
            print(f"{e} is not coprime to phi({n})={phi}, Try another random integer between 2 and {phi-1}")
    # e = 313

    print("e =", e)
    # step 5 --> Calculate the private key d = e^-1 (mod phi(n))
    # d = modInverse(phi, e)
    d = pow(e, -1, phi)  #Calculating the multiplicative inverse of e modulo phi(n)
    print(f"phi({n}) = {phi}")
    print("d =", d)
    print(f'Public key: {e, n}')
    print(f'Private key: {d}')

    return e, d, n
    # return 35535, d, n


def Signing(msg, d, n):
    # S = M^d mod n, here M = Message
    S = mod_power(msg, d, n)
    return S

def mod_power(a, n, m):
    r = 1  #r is the output value or return value
    # y = a % m , here y is y0, since it will be done anyway in line 84, we omit this line And since y is not used any further, we can replace yi with a
    while n > 0:
        if n & 1 == 1:  #Here, we grab every bit b0, b1, b1,..,bt and move them to the LSB position, when bitwise-and with ...0001, All the bits except the LSB bit is 0ed,
            # only the LSB bit is preserved.
            #Then we right shift the n by 1 (line 85) so that the next bit position b1 comes to the LSB position, in this way we traverse the binary digits in reverse order(from b0 to bt), we do this until all the bit values becomes 0 in which case bi becomes 0, and we break out of the while loop
            r = (r * a) % m #Same as product of yi(mod m) if the corresponding bit value is 1
        a = (a * a) % m #same as yi + 1 = (yi)^2 the recurrence relation we established on slide, it needs to be done for every bit position no matter what(bi can be 0 or 1)
        n >>= 1 #Every time, I advance the bit position further
    return r


def Verifying(S, e, n):
    # M' = S^e mod n
    msgPrime = mod_power(S, e, n)
    return msgPrime


def main():
    msg = int(input(f"Enter the message(in numerical value): "))
    print(f'Original message:{msg}')
    # This routine creates the public and private key at the receiver side
    e, d, n = keyGeneration()
    signature = Signing(msg, d, n)
    print(f'Signature is: {signature}')
    msgPrime = Verifying(signature, e, n)
    print(f"Calculated message from the received signature: {msgPrime}")
    # If M' == M, then the signature is verified, otherwise the signature is forgery signature
    if msgPrime != msg:
        print(f"The message signature {signature} is a forgery signature!!!!")
    else:
        print(f'Signature {signature} is verified successfully.')

if __name__ == '__main__':
    main()