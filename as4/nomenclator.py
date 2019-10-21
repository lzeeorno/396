#question2

import random
#function of encryptMessage with subKey
def encryptMessage(subKey, codeBook, message):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wordList = message.split(' ')
    for i in range(len(wordList)):
        transWord=''
        #if letter is upper case
        if wordList[i].upper() in codeBook:
            wordList[i] = random.choice(codeBook[wordList[i].upper()])
            #if letter is lower case
        elif wordList[i].lower() in codeBook:
            wordList[i] = random.choice(codeBook[wordList[i].lower()])
        elif wordList[i].title() in codeBook:
            wordList[i] = random.choice(codeBook[wordList[i].title()])
        else:
            for symbol in wordList[i]:
                if symbol.upper() in letters:
                    symIndex = letters.find(symbol.upper())
                    if symbol.isupper():
                        transWord += subKey[symIndex].upper()
                    else:
                        transWord += subKey[symIndex].lower()
                else:
                    transWord += symbol
            wordList[i] = transWord
    return ' '.join(wordList)


def decryptMessage(subKey, codeBook, message):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wordList = message.split(' ')
    for i in range(len(wordList)):
        transWord=''
        #symbol handle problem
        if wordList[i].replace(',','').replace("'",'').replace('.','').isalpha():
            for symbol in wordList[i]:
                if symbol.upper() in subKey:
                    symIndex = subKey.find(symbol.upper())
                    if symbol.isupper():
                        transWord += letters[symIndex].upper()
                    else:
                        transWord += letters[symIndex].lower()
                else:
                    transWord += symbol
            wordList[i] = transWord
        else:
            for key in codeBook:
                if wordList[i] in codeBook.get(key):
                    wordList[i] = key
    return ' '.join(wordList)
