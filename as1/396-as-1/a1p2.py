# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math#,pyperclip

def main():
    myMessage = 'ADGCFBE'
    myKey = [1,3,2]

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

   #pyperclip.copy(ciphertext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(len(key))))
    # The number of "rows" in our grid will need:
    numOfRows = len(key)
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [[''for i in range(numOfRows)]for i in range(numOfColumns)]
    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0
    for symbol in message:
        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and (key[row]-1) >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1;
        plaintext[column][key[row]-1] = symbol
        column += 1 # Point to next column.
     
        
    
    

    answerprint=''
    for i in range(numOfColumns):
        answerprint += ''.join(plaintext[i])
    return answerprint


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
