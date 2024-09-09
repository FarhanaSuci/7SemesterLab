#This is a python program for Ceaser Cipher
def encrypt(message, key):
    #result is the final encrypted message
    result = ""
    #Run a loop for each character of the plaintext
    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif (char.islower()):
            #We need to subtract 32 for showing the ciphertext in capital letter
            result += chr((ord(char) + key - 97) % 26 + 97)
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
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) - key - 97) % 26 + 97)
        else: #if the plaintext character contains the space character
            result += char

    return result



def main():
    plainText = input("Enter the plaintext: ")
    key = 3 #For Ceaser Cipher the shift key will always be 3
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


