alphabets = "abcdefghijklmnopqrstuvwxyz "
letter_to_index = dict(zip(alphabets, range(len(alphabets))))
index_to_letter = dict(zip(range(len(alphabets)), alphabets))


# print(letter_to_index)
# print(index_to_letter)

# The encrypt method
def encrypt(message, key):
    encrypted = ''
    # First we need to split the main message into blocks of size key length
    # We use list comprehension here
    split_message = [message[i: i + len(key)] for i in range(0, len(message), len(key))]

    # We need to add the key stream to each split portion of the message
    for split in split_message:
        i = 0
        for letter in split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabets)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


# The decrypt method
def decrypt(cipher, key):
    decrypted = ''
    # First we need to split the main message into blocks of size key length
    # We use list comprehension here
    split_cipher = [cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))]

    # We need to add the key stream to each split portion of the message
    for split in split_cipher:
        i = 0
        for letter in split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabets)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def main():
    plainText = input("Enter the plaintext: ")
    keyStream = input("Enter the keystream: ")
    cipherText = encrypt(plainText, keyStream)
    decryptedPlainText = decrypt(cipherText, keyStream)

    print(f"Original Message: {plainText}")
    print(f"Encrypted Message: {cipherText}")
    print(f"Decrypted Message: {decryptedPlainText}")


main()
