#This is a python program for Ceaser Cipher
import math
def encrypt(message, key1, key2):
    #result is the final encrypted message
    result = ""
    finalResult = ""
    #Run a loop for each character of the plaintext
    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            #The formula is : T = (P * K1) mod 26
            #                 C = (T + K2) mod 26
            # mi = modInverse(26,key1)
            result = chr(((ord(char) - 65) * key1) % 26 + 65)
            #Then perform the additive cipher on the previous result
            result = chr((ord(result) + key2 - 65) % 26 + 65)
            #Add the resulting character with the finalResult
            finalResult += result


        elif (char.islower()):
            result = chr(((ord(char) - 97) * key1) % 26 + 97)
            #Then perform the additive cipher on the previous result
            result = chr((ord(result) + key2 - 97) % 26 + 97)
            finalResult += result
        else: #if the plaintext character contains the space character
            finalResult += char

    return finalResult

def decrypt(message, key1, key2):
    #result is the final encrypted message
    result = ""
    finalResult = ""
    #Run a loop for each character of the plaintext
    for i in range(len(message)):
        char = message[i]

        if char.isupper():
            #The formula is : T = (C - K2) mod 26
            #                 P = (T * K1 inverse) mod 26
            # mi = modInverse(26, key1)
            mi = pow(key1, -1, 26)
            if not mi is None:
                # Add the additive inverse cipher to the ciphertext
                result = chr((ord(char) - key2 - 65) % 26 + 65)
                # Then multiply the multiplicative inverse with the previous result
                result = chr(((ord(result) - 65) * mi) % 26 + 65)
                finalResult += result
            else:
                print(
                    f"Sorry!!!The multiplicative inverse of {key1} modulo 26 does not exits. Can't decrypt the message!")
                return None
        elif char.islower():
            # mi = modInverse(26, key1)
            mi = pow(key1, -1, 26)
            if not mi is None:
                #Add the additive inverse cipher to the ciphertext
                result = chr((ord(char) - key2 - 97) % 26 + 97)
                #Then multiply the multiplicative inverse with the previous result
                result = chr(((ord(result) - 97) * mi) % 26 + 97)
                finalResult += result
            else:
                print(f"Sorry!!!The multiplicative inverse of {key1} modulo 26 does not exits. Can't decrypt the message!")
                return None
        else: #if the plaintext character contains the space character
            finalResult += char

    return finalResult

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
        if t1 < 0:
            while t1 < 0:
                t1 += 26
                return t1
        else:
            return t1
        # return t1
    else:
        return None



# def main():
#     plainText = input("Enter the plaintext: ")
#     key1 = int(input("Enter the key value for multiplicative cipher: "))
#     key2 = int(input("Enter the key value for additive cipher: "))
#     cipherText = encrypt(plainText, key1, key2)
#     cipher = ''
#     #print(f"The encrypted message is : ", end="")
#     for letter in cipherText:
#         # We need to subtract 32 for showing the ciphertext in capital letter
#         cipher += letter.upper()
#
#     #print(f"The encrypted message is: {cipherText}")
#     print(f"The encrypted message is: {cipher}")
#     decryptedPlaintext = decrypt(cipherText, key1, key2)
#     print(f"The decrypted message is : {decryptedPlaintext}")

def main():
    plainText = ''
    #Take the file input
    with open("AffineInput.txt", "r") as rf:
        with open("secretkey.txt", "r") as rf2:

            with open("Encrypted.txt", "w") as wf:
                for letter in rf:
                    plainText += letter

                Keys = rf2.readline().split(" ")
                # print(Keys)
                key1 = Keys[0]
                key2 = Keys[1]
                key1 = int(key1)
                key2 = int(key2)
                # print(type(key1))
                # print(key1, end='')
                # print(key2, end='')
                print(plainText)

                # plainText = plainText[:len(plainText)-1]
                # print(plainText, end='')
                # print(key1)
                # print(key2)
                cipherText = encrypt(plainText, key1, key2)
                # cipher = ''
                # for letter in cipherText:
                #     cipher += letter.upper()
                wf.write("The encrypted message is: "+cipherText.upper())
                #We need to position the file pointer to the begining of the file Encrypted.txt
                # with open("Encrypted.txt", "r") as rf2:
                    #rf2.seek(0) #We need to position the file pointer to the begining of the file Encrypted.txt
                with open("Decrypted.txt", "w") as wf2:
                        # cipherText = rf2.readline()
                        # print(cipherText)
                    decryptedPlaintext = decrypt(cipherText, key1, key2)
                    wf2.write(f"The decrypted message is : {decryptedPlaintext}")





if __name__ == "__main__":
    main()


