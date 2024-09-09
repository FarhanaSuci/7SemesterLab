import copy, math
alphabet = 'abcdefghijklmnopqrstuvwxyz '
# encryptionKey = {3: 1, 1: 2, 4: 3, 5: 4, 2: 5}
decryptionKey = {1: 3, 2: 1, 3: 4, 4: 5, 5: 2}
encryptionKey = [2,0,3,4,1]
decryptionKey = [1,4,0,2,3]
# encryptionKey = [3,2,0,1,4,5,6]
# decryptionKey = [0,1,2,3,4,5,6]
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

print(letter_to_index)
print(index_to_letter)
#How to define 2D list in python
# rows, cols = (5, 5)
# arr = [[0 for i in range(cols)] for j in range(rows)]
# print(arr)
def encryption(message, keyword):
    key = int(keyword) #Converting the numeric string into an integer
    splitmessage = [message[i:i+key] for i in range(0, len(message), key)]
    print(f"Spliited Message List: {splitmessage}")
    table = [['z' for i in range(key)] for j in range(len(splitmessage))]
    # print(table)
    #Step1: Entering the message characters in the table row by row.
    for rows in range(len(splitmessage)):
        i = rows
        j = 0
        for cols in range(key):
            if j < len(splitmessage[i]):
                table[rows][cols] = splitmessage[i][j]
                j = j + 1

    print(f"Table after reading row by row : {table}")
    #Take the copy of the table
    copyTable = copy.deepcopy(table)
    # print(table)
    # print(copyTable)
    #Step2 : Reorder the table column according to the encryption key
    # encryptionKey = {3: 1, 1: 2, 4: 3, 5: 4, 2: 5}
    for row in range(len(copyTable)):
        for j in range(len(copyTable[row])):
            copyTable[row][j] = table[row][encryptionKey[j]]

    # print(copyTable)
    print(f"Table after reordering according to the encryption key: {copyTable}")
    # Step3 : Now we read the table column by column
    cipher = ''
    for cols in range(len(copyTable[0])): #cols = 0 to 4
        for rows in range(len(copyTable)): #rows = 0 to 2
            cipher += copyTable[rows][cols]

    print(cipher)
    return cipher, copyTable


def decryption(message, keyword, table):
    key = int(keyword) #Converting the numeric string into an integer
    # splitmessage = [message[i:i+key] for i in range(0, len(message), key)]
    # print(splitmessage)
    #
    # table = [['z' for i in range(key)] for j in range(len(splitmessage))]
    splitmessageforDecrypt = [message[i:i+len(table)] for i in range(0, len(message), len(table))]
    print(splitmessageforDecrypt)
    # columnTable = [[0 for i in range(key)] for j in range(len(splitmessage))]
    columnTable = [[0 for i in range(key)] for j in range(math.ceil(len(message) / key))]

    #Step1: Entering the message characters in the table column by column.
    for cols in range(key): #Key = 5, [0,1,2,3,4]
        i = cols
        j = 0
        for rows in range(len(table)): #len(table) = 4 [0,1,2,3]
            # if j < len(splitmessage[i]):
                columnTable[j][i] = splitmessageforDecrypt[i][j]
                j = j + 1
    print(f"Table after reading column by column : {columnTable}")
    #Step2 : Reorder the matrix according to the decryption key
    #Take the copy of the table
    copyTable = copy.deepcopy(columnTable)
    # print(table)
    # print(copyTable)
    #Step2 : Reorder the table column according to the decryption key
    # encryptionKey = {3: 1, 1: 2, 4: 3, 5: 4, 2: 5}
    for row in range(len(copyTable)):
        for j in range(len(copyTable[row])):
            copyTable[row][j] = columnTable[row][decryptionKey[j]]

    print(f"Table after reordering according to the decryption key: {copyTable}")

    #Step 3: read the table row by row
    decryptedPlainText = ''
    for rows in range(len(copyTable)):
        for cols in range(len(copyTable[rows])):
            decryptedPlainText += copyTable[rows][cols]

    # print(decryptedPlainText)
    return decryptedPlainText
def main():
    message = input("Enter the plaintext: ")
    key = input("Enter the key(group size or column size): ")

    cipherText, table = encryption(message, key)
    # cipherText = encryption("I am Shafi.", "5")
    print(f"The encrypted ciphertext is: {cipherText.upper()}")
    plaintext = decryption(cipherText, key, table)
    print(f"The decrypted plaintext is: {plaintext.lower()}")



main()