# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
import sys


# The string to be encrypted/decrypted:
message = sys.argv[3:]
message = ' '.join(message)



# The encryption/decryption key:
key = sys.argv[1]
key_length = len(key)

if sys.argv[2] != 'encrypt' and sys.argv[2] != 'decrypt':
    print('Please enter encrypt or decrypt!')
    sys.exit(0)
# Whether the program encrypts or decrypts:
mode = sys.argv[2] # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Stores the encrypted/decrypted form of the message:
translated = ''
last_shift = 0
count = 0
for symbol in message:
    keyIndex = SYMBOLS.find(key[count%key_length].upper())

    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol.upper() in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol.upper())
        keyIndex = keyIndex + last_shift
        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + keyIndex
            last_shift = keyIndex
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - keyIndex
            last_shift = keyIndex

        # Handle wrap-around, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex % len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex % len(SYMBOLS)

        if symbol.isupper():
            translated = translated + SYMBOLS[translatedIndex].upper()
        else:
            translated = translated + SYMBOLS[translatedIndex].lower()
	count += 1
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)

