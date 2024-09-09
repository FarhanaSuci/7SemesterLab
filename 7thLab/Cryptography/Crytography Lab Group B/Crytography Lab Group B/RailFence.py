def main():
    print("RailFenceCipher_Demo")

    print()

    clearText = "Hello World!"
    print("Original Text: " + clearText)
    print()

    key = 3 #Key works as the depth of the Rail-Fence Cipher

    cipherText = cipher(clearText, key)
    print("Ciphered Text: {0}".format(cipherText))

    decipherText = decipher(cipherText, key)
    print("Deciphered Text: {0}".format(decipherText))

    return


def cipher(clearText, key):
    result = ""

    matrix = [["" for x in range(len(clearText))] for y in range(key)] # list comprehension --youtube

    increment = 1
    row = 0
    col = 0

    for c in clearText:
        if row + increment < 0 or row + increment >= len(matrix):
            # When the row counter reaches the last row, then increment becomes -1 so that
            # The row counter points to the row before the last in the next iteration.
            # When the row counter reaches first row, the increment becomes 1 so that
            # The row counter points to the row after the first in the next iteration.
            # At every iteration, the column counter will always increment by 1
            increment = increment * -1

        matrix[row][col] = c

        row += increment
        col += 1

    for list in matrix:
        result += "".join(list)  #We convert each list into a string

    return result


def decipher(cipherText, key):
    result = ""

    matrix = [["" for x in range(len(cipherText))] for y in range(key)]

    # Here idx works as the index position of the ciphertext
    idx = 0
    increment = 1

    for selectedRow in range(0, len(matrix)):
        row = 0

        for col in range(0, len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                # When the row counter reaches the last row, then increment becomes -1 so that
                # The row counter points to the row before the last in the next iteration.
                # When the row counter reaches first row, the increment becomes 1 so that
                # The row counter points to the row after the first in the next iteration.
                # At every iteration, the column counter will always increment by 1
                increment = increment * -1
            # We traverse the matrix in zig-zag order and in the first iteration of the
            # outer loop, we fill in the ciphertext value in the first row position
            # In the 2nd  iteration of the outer loop, we fill in the ciphertext value in
            # the 2nd row position and so on.

            if row == selectedRow:
                matrix[row][col] += cipherText[idx]
                idx += 1

            row += increment

    matrix = transpose(matrix)   #Instead of transposing, we can traverse in zig-zag way to build the ciphertext
    for list in matrix:
        result += "".join(list)

    return result


def transpose(m):
    # Here m is the cipher matrix of size 3 by 12
    # Here, we create a matrix of size 12 by 3,
    # so len(m[0]) = 12 is the number of rows and
    # len(m) = 3 is the number of columns
    result = [[0 for y in range(len(m))] for x in range(len(m[0]))]
    # Here, in the for loop, we traverse each element of the cipher matrix m
    for i in range(len(m)):
        for j in range(len(m[0])):
            # We transpose the matrix m[i][j], so row i of "m" matrix
            # becomes column "i" of ressult matrix and vice-versa
            result[j][i] = m[i][j]

    return result


main()