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

            result += chr(((ord(char) - 65) * pow(key, -1, 26)) % 26 + 65)

        elif (char.islower()):

            result += chr(((ord(char)- 97) * pow(key, -1, 26)) % 26 + 97)

        else: #if the plaintext character contains the space character just concatenate it
            result += char

    return result


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