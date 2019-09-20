# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import random, sys, a1p1, a1p2

def main():
    random.seed(42) # set the random "seed" to a static value

    for i in range(5): # run 5 tests
        # Generate random messages to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it.
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # convert list to string

        print('Test #%s: "%s..."' % (i+1, message[:50]))
        print(len(message))
        for i in range(int(len(message)/2)):
            keylength = i + 1
            key = []
            for n in range(keylength):
                key.append(n + 1)

            for x in range(5):
                random.shuffle(key)
                print('key =',end=' ')
                print(key)
                encrypted = a1p1.encryptMessage(key, message)
                decrypted = a1p2.decryptMessage(key, encrypted)
                if message != decrypted:
                        print('Mismatch with key %s and message %s.' % (key, message))
                        print('Decrypted as: ' + decrypted)
                        sys.exit()

                print('Transposition cipher test passed.')




# If transpositionTest.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
