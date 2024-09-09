#This is a python program for Ceaser Cipher
import math
def encrypt(message, key):
    #result is the final encrypted message
    result = ""
    #Run a loop for each character of the plaintext
    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            #The formula is : (plaintext character * key) mod 26
            result += chr(((ord(char) - 65) * key) % 26 + 65)
        elif (char.islower()):
            #We need to subtract 32 for showing the ciphertext in capital letter
            result += chr(((ord(char) - 97) * key) % 26 + 97)
        else: #if the plaintext character contains the space character
            result += char

    return result

def decrypt(message, key):
    #result is the final encrypted message
    result = ""
    #Run a loop for each character of the plaintext
    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            # The formula is : (ciphertext character * modInverse of key modulo 26)) mod 26
            mi = modInverse(26,key)
            if not mi is None:
                result += chr(((ord(char) - 65) * mi) % 26 + 65)
            else:
                print(f"Sorry!!!The multiplicative inverse of {key} modulo 26 does not exits. Can't decrypt the message!")
                return None
            # result += chr(((ord(char) - 65) * mi) % 26 + 65)
        elif (char.islower()):
            #result += chr((ord(char) * mi - 97) % 26 + 97)
            mi = modInverse(26,key)
            if not mi is None:
                result += chr(((ord(char)- 97) * mi) % 26 + 97)
            else:
                print(f"Sorry!!!The multiplicative inverse of {key} modulo 26 does not exits. Can't decrypt the message!")
                return None
            # result += chr(((ord(char) - 97) * mi) % 26 + 97)
        else: #if the plaintext character contains the space character just concatenate it
            result += char

    return result

def modInverse(r1, r2):
    t1, t2 = 0, 1
    while(r2 > 0):
        q = math.floor(r1 / r2)
        r = r1 - q * r2
        #Adjusting the value of r1 and r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t

    # print(f"The r1 value : {r1}")
    if(r1 == 1):
        #The multiplicative inverse exists
        return t1
    else:
        return None





def main():
    plainText = input("Enter the plaintext: ")
    key = int(input("Enter the shift key value: "))
    cipherText = encrypt(plainText, key)
    # print(f"The encrypted message is : ", end="")
    # for letter in cipherText:
    #     # We need to subtract 32 for showing the ciphertext in capital letter
    #     ch = cipherText[letter]
    #     char = chr(ord(ch) - 32)
    #     print(char, end="")
    print(f"The encrypted message is: {cipherText}")
    decryptedPlaintext = decrypt(cipherText, key)
    print(f"The decrypted message is : {decryptedPlaintext}")

if __name__ == "__main__":
    main()