# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import time, os, sys, a1p1, a1p2

def main():
    inputFilename = 'mystery.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    outputFilename = 'encrypted.txt'
    myKey = [2,4,6,8,10,1,3,5,7,9]
    myMode = 'decrypt' # set to 'encrypt' or 'decrypt'

    # If the input file does not exist, then the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = a1p1.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = a1p2.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
