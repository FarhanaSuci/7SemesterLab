import random, math, copy

def keyGeneration(plainTextLen, permute):
     #Step1 --> Create a super-increasing tuple, for now I create it manually
     # b = []
     # sum = 0
     # b.append(7)
     # sum = 7
     # for i in range(plainTextLen):
     #     bi =  random.randint(8, 500)
     #     while bi >= sum:
     #         sum = sum + bi
     #         b.append(bi)
     #         break
     b = [7, 11, 19, 39, 79, 157, 313]
     #calculate the sum of the elements of b
     sum = 0
     for i in range(len(b)):
         sum = sum + b[i]
     print(f"Sum: {sum}")
     #Step2 --> Choose a modulo n > b1 + b2 + ... + bn
     n = random.randint(sum + 1, sum + 300)
     print(f"n = {n}")
     #Step3 --> Choose a random integer m such that m is relatively prime to n and 1 <= r <= (n - 1)
     #randint() function's start and stop index both are inclusive
     r = random.randint(1, n-1)
     while math.gcd(r, n) != 1:
         print(f"Oops! You choose a number {r} that is not relatively prime to {n}, Try another!!!")
         r = random.randint(1, n-1)

     print(f"m = {r}")
     #Step4 --> create a temporary K-tuple t = [t1, t2, ..., tk] in which ti = (r * bi) mod n
     t = []
     #For Testing Purpose
     # n, r = 900, 37

     for i in range(plainTextLen):
         ti = (r * b[i]) % n
         t.append(ti)

     copyTable = copy.deepcopy(t)
     print(f"The temporary k-tuple t: {t}")
     #Step5 --> a = permute(t)
     a = []
     for i in range(len(copyTable)):
         a.append(copyTable[permute[i] - 1])

     print(f"Public Key,a = {a}")
     print(f"Private Key, n = {n}, r = {r}, b = {b}")

     return a, n, r, b


def KnapsackSum(x, a):
    s = 0
    k = len(x)
    for i in range(k):
        s = s + a[i] * x[i]

    return s


def encryption(plainText, a):
    #Step1 --> Create the x-tuple x = [x1, x2, x3, ..., xk] from plaintext
    x = []
    for i in range(len(plainText)):
        x.append(int(plainText[i]))

    print(f"The x-tuple is: {x}")
    #Step2 --> Call the KnapsackSum() routine
    s = KnapsackSum(x, a)
    #Return the value of s as the ciphertext
    return s


def inv_KnapsackSum(s, a):
    x = []
    k = len(a)
    #Traverse the s list in decreasing order
    for i in range(k-1, -1, -1):
        if s >= a[i]:
            x.append(1)
            s = s - a[i]
        else:
            x.append(0)

    print(f"x = {x}")
    return x



def decryption(s, b, r, n, a, permute):
    #Step1 --> Calculating s' = (r^-1 * s) mod n
    #Step1.1 --> Calculate r^-1 mod n, we use Extended Euclidean Algorithm
    rInverse = modInverse(n, r)
    sPrime = (rInverse * s) % n
    print(f"SPrime = {sPrime}")
    xPrime = inv_KnapsackSum(sPrime, b)
    print(f"xPrime = {xPrime}")
    copyTable2 = copy.deepcopy(xPrime)
    x = []
    for i in range(len(copyTable2)):
        x.append(copyTable2[permute[i] - 1]) #Since, indexing starts from 0, we subtract 1

    print(f"After Permutation The x: {x}")
    return x

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

    plainText = input("Enter the plaintext character: ")
    plainText = bin(ord(plainText)).replace("0b", "")
    print(plainText)
    permutationTable = [4, 2, 5, 3, 1, 7, 6]
    #a is the Public Key used by Alice
    #n, r, b are the private Keys used by Bob
    a, n, r, b = keyGeneration(len(plainText), permutationTable)
    cipherText = encryption(plainText, a)
    print(f"CipherText: {cipherText}")
    decryptedPlainText = decryption(cipherText, b, r, n, a, permutationTable)
    #This for loop converts each int type value of the list into str type, needed for join() function
    for i in range(len(decryptedPlainText)):
        decryptedPlainText[i] = str(decryptedPlainText[i])
    decryptedPlainText.insert(0, "0b")
    decryptedPlainText = "".join(decryptedPlainText) #Convert the list into String
    decryptedPlainTextInDecimal = int(decryptedPlainText, 2)
    decryptedPlainTextInASCII = chr(decryptedPlainTextInDecimal)
    print(f"Decrypted PlainText in Binary Format : {decryptedPlainText}")
    print(f"Decrypted Plaintext in Decimal Format: {decryptedPlainTextInDecimal}")
    print(f"Decrypted Plaintext in ASCII Format: {decryptedPlainTextInASCII}")



if __name__ == '__main__':
    main()