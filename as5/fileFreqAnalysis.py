
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def freqDict(f1, frequency):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    op = open(f1)
    cipher = op.read()
    op.close()
    for letter in cipher:
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

def freqDecrypt(f1, f2, frequency):
    mapping = freqDict(f1, frequency)
    
    freqToLetter = {}
    for letter in LETTERS:
        if mapping[letter] not in freqToLetter:
            freqToLetter[mapping[letter]] = [letter]
        else:
            freqToLetter[mapping[letter]].append(letter)

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=frequency.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
        
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=takeFirst, reverse=True)
    
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
    freq = ''.join(freqOrder)
    op = open(f1)
    cipher = op.read()
    op.close()
    final = ''
    for letter in cipher:
        if letter in freq:
            final += frequency[freq.find(letter)]
        else:
            final += letter
    op = open(f2, 'w')
    op.write(final)
    op.close()

def takeFirst(item):
    return item[0]
        
