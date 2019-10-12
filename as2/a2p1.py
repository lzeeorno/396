# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
import sys


# The string to be encrypted/decrypted:
message = "esi n ehohe hoe hi ldvhonsdlAtcadosr rctf ias au scb dc b'p,o,ntepcetrcdtrypnr fa'uilaalmn  ga r pnn prpaee Caror tEtiaeginoev iemsy iura e."
# sys.argv[3:]
message = ' '.join(message)
#message = eval(message)

keylist = [1,2,3,4,5,6,7,8,9]
# Whether the program encrypts or decrypts:
mode = 'decrypt'
# sys.argv[2] # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Stores the encrypted/decrypted form of the message:
translated = ''
# The encryption/decryption key:
for k in keylist:
    key = k

# if sys.argv[2] != 'encrypt' and sys.argv[2] != 'decrypt':
#     print('Please enter encrypt or decrypt!')
#     sys.exit(0)




    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            if symbol.isupper():
                translated = translated + SYMBOLS[translatedIndex].upper()
            else:
                translated = translated + SYMBOLS[translatedIndex].lower()
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Output the translated string:
    print(translated)
    print("")
