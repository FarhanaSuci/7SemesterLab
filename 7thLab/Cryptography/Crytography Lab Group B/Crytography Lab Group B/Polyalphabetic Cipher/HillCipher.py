"""
Implementation of Hill Cipher!

Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)

C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used

"""

import numpy as np
from egcd import egcd  # pip install egcd

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def matrix_mod_inv(matrix, modulus):
    """We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
    """
    #Here we calculate the determinant of matrix via np.linalg.det(matrix), since this method calculate the
    #result numerically, we need to round off the result to avoid round-off error
    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    #Here we calculate the determinant inverse modulo 26 via extended Euclidean Algorithm
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    #Adjoint matrix = determinant * (inverse of matrix)
    #Matrix modulo inverse(K^-1) = determinantInverse * Adjoint matrix
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus )  # Step 3)

    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        #Convert each character of the message to equivalent ascii value
        message_in_numbers.append(letter_to_index[letter])

    #Here we split the numerical message list into blocks of matrix of size m
    split_P = [message_in_numbers[i : i + int(K.shape[0])] for i in range(0, len(message_in_numbers), int(K.shape[0]))]

    for P in split_P:
        #np.asarray(P) returns a row vector, we need to convert it to column vector via np.transpose() method
        #to be able to multiply it with the key matrix
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        #To create m-size blocks, we need to add bogus letter, if
        #P.shape[0] = 1 but K.shape[0] = 2, we need to add one extra bogus letter
        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        #np.dot(K, P) % len(alphabet) performs the multiplication (K * P) mod 27
        numbers = np.dot(K, P) % len(alphabet)
        #The result of the multiplication is a column vector of size 3 by 1
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            #here we add each row value of the column vector numbers
            #we do the followings: numbers[0][0] + numbers[1][0] + numbers[2][0] for column vector of size 3 by 1
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [cipher_in_numbers[i : i + int(Kinv.shape[0])] for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        #the formula is: (P = (K^-1 * C) mod 26)
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


def main():
    # message = 'my life is potato'
    #message = "help"
    message = input("Enter the plaintext: ")

    #K = np.matrix([[3, 3], [2, 5]])
    #K = np.matrix([[6, 24, 1], [13,16,10], [20,17,15]]) # for length of alphabet = 26
    K = np.matrix([[3,10,20],[20,19,17], [23,78,17]]) # for length of alphabet = 27
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)


main()