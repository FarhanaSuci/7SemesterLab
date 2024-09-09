import math,random

def keyGeneration(p, q):
    # step 2 --> Calculate n = p * q
    n = p * q
    print("n =", n)

    # step 3 --> calculate phi(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # step 4 --> select an integer e such that 1 < e < phi(n) and e is coprime to phi(n)
    while True:
        e = random.randint(2, phi)
        print(f"The random integer e: {e}")
        # checking whether e is coprime to phi(n)
        if (math.gcd(e, phi) == 1):
            break
        else:
            print(f"{e} is not coprime to phi({n})={phi}, Try another random integer between 2 and {phi}")

    print("e =", e)
    # step 5 --> Calculate the private key d = e^-1 (mod phi(n))
    d = modInverse(phi, e)
    # d = modInverse(phi, 13)
    print(f"phi({n}) = {phi}")
    print("d =", d)
    print(f'Public key: {e, n}')
    print(f'Private key: {d, n}')

    return e, d, n
    # return 13, d, n

def encrypt(P, e, n):
    # C = pow(P, e)
    # C = math.fmod(C, n)  #CipherText = P^e mod n
    C = mod_power(P, e, n)
    # C = power(C, e, n)
    # C = math.pow(P, e) % n
    return C

def decrypt(C, d, n):
    # decryption
    # M = pow(C, d)
    # Here we need to use fast modular exponentiation algorithm
    # YouTube Video Link: https://www.youtube.com/watch?v=3Bh7ztqBpmw
    # M = math.fmod(M, n) #Plaintext = C^d mod n
    M = mod_power(C, d, n)
    # M = power(M, d, n)
    # M = math.pow(C, d) % n
    return M

def power(x, y, p):
    res = 1  # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % p

    if (x == 0):
        return 0

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res

def mod_power(a, n, m):
    r = 1
    while n > 0:
        if n & 1 == 1:
            r = (r * a) % m #Same as product of yi if the corresponding bit value is 1
        a = (a * a) % m #Every time, I advance the bit position further, same as yi + 1 = (yi)^2
        n >>= 1
    return r

def modInverse(r1, r2):
    temp = r1
    t1, t2 = 0, 1
    while (r2 > 0):
        q = math.floor(r1 / r2)
        r = r1 - q * r2
        # Adjusting the value of r1 and r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t

    # print(f"The r1 value : {r1}")
    if (r1 == 1):  # If gcd = 1, then multiplicative inverse exists
        # The multiplicative inverse exists
        if t1 < 0:
            while t1 < 0:
                t1 += temp
            return t1
        else:
            return t1
        # return t1
    else:
        return None

def main():
    p = int(input(f"Enter first large prime number p: "))
    q = int(input(f"Enter second large prime number q: "))
    msg = int(input(f"Enter the message(in numerical value): "))
    print(f'Original message:{msg}')
    # This routine creates the public and private key at the receiver side
    e, d, n = keyGeneration(p, q)
    cipherText = encrypt(msg, e, n)
    print(f'Encrypted message: {cipherText}')
    decryptedPlainText = decrypt(cipherText, d, n)
    print(f'Decrypted message: {decryptedPlainText}')

if __name__ == '__main__':
    main()
