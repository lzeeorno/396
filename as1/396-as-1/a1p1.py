# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# edit1: Since the key is not unique, but a list of integers
# edit2: same reason of edit1
# edit3: set a pointer to decide the order of adding character in ciphertext
# edit4:since we want to cipher as column


def main():
    myMessage = 'CIPHERS ARE FUN'
    myKey = [2, 4, 1, 5, 3]

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')





def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * len(key)#edit1
    index = -1; #edit3

    # Loop through each column in ciphertext.
    for column in key: #edit2
        currentIndex = column - 1
        index+=1
        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[index] += message[currentIndex]

            # move currentIndex over
            currentIndex += len(key) #edit4

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
