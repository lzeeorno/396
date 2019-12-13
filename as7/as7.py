import vigenereCipher, detectEnglish, vigenereHacker
import sys, re, os

ENG_LETT_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 
'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 
'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 
'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenereKeySolver(ciphertext, key_len):
    #split the ciphertext by the key length 
    keyIndex = 0
    splitText = [""] * key_len
    for i in range(0, len(ciphertext)):
        if ciphertext[i].isalpha():
            #if the letter is english make all letter as capital letter
            character = ciphertext[i].upper()
            if keyIndex < key_len:
                splitText[keyIndex] += character
                keyIndex = keyIndex + 1
            else:
                keyIndex = 0
                splitText[keyIndex] += character
                keyIndex = keyIndex + 1

    imc_list = []
    for i in range(0, len(splitText)):
        subString = splitText[i]
        imc_subString = []
        # 26 possible key in each sub string 
        for possible_key in LETTERS:
            deciphered_subString = vigenereCipher.decryptMessage(possible_key, subString)
            count_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

            for index in range(0, len(deciphered_subString)):
                current_letter = deciphered_subString[index]
                count_dict[current_letter] = count_dict[current_letter] + 1

            imc = 0
            #calculate the imc value by the formula
            for letter in count_dict:
                t_value = count_dict[letter] / len(deciphered_subString)
                e_value = ENG_LETT_FREQ[letter] / 100
                imc += t_value * e_value

            key_imc_tuple = (possible_key, imc)
            imc_subString.append(key_imc_tuple)
            #print(imc_subString)
        for n in range(0, len(imc_subString)):
            for m in range(len(imc_subString)-1, n, -1):
                if imc_subString[m-1][1] < imc_subString[m][1]:
                    imc_subString[m], imc_subString[m-1] = imc_subString[m-1], imc_subString[m]
    
        imc_list.append(imc_subString)
    #print(imc_list)
    keys_list = []
    #find 10 possible keys 
    for i in range(0, 10):
        current_key = ""
        for m in range(0, key_len):
            current_key = current_key + imc_list[m][0][0]
        keys_list.append(current_key)

        min_difference = float(imc_list[0][0][1])
        #replace the by the difference 
        for i in range(0, key_len):
            current_difference = imc_list[i][0][1] - imc_list[i][1][1]
            if current_difference < min_difference:
                min_difference_index = i
                min_difference = current_difference
        #delete one let next key become first key
        del(imc_list[min_difference_index][0])

    return keys_list
'''
question2
'''
def hackVigenere(string):
    #set a accurancy for apply in detectEnglish
    accurancy = 0
    current_acc = 0
    #get some possible key length for decipher key
    poss_KeyLength = keyLengthIC(string, 5)
    for length in poss_KeyLength:
        #get some possible keys by the input some possible key length
        poss_keys = vigenereKeySolver(string, length)

        for key in poss_keys:
            solution = vigenereCipher.decryptMessage(key, string)
            curr_accurancy = detectEnglish.getEnglishCount(solution)
            if curr_accurancy > accurancy:
                accurancy = curr_accurancy
                real_key = key
    return real_key


'''
The following functions are
cited from personal Assignment 6 
'''
def stringIC(inputstr):
    fre_count = {}#store every letter's frequency
    IC = 0
    for c in inputstr:
        if c.upper() not in fre_count:#if fre_count dont have c.upper() as key 
            fre_count[c.upper()]=1    #add c.upper() to fre_count and value = 1
        else:
            fre_count[c.upper()]+=1   #find another c.upper() in input, than frequency + 1
    
    for key in fre_count.keys():
        IC += fre_count[key]*(fre_count[key]-1) #ci(ci − 1)

    if len(inputstr) <= 1:#input len = 1
        return 0
    else:
        return IC/(len(inputstr)*(len(inputstr)-1)) #IC/N(N-1) N=len(inputstr)
        

def subseqIC(ciphertext, keylen):
    IC = 0; #store sum of IC
    for i in range(keylen):
        message = vigenereHacker.getNthSubkeysLetters(i+1, keylen, ciphertext)#every nth letter for each keyLength set of letters in text
        IC += stringIC(message) #calculate IC of message and add it with IC
    
    return IC/keylen

def keyLengthIC(ciphertext, n):
    ICdict = {} #store IC and length of key
    for i in range(1, 21):#key length
        IC = subseqIC(ciphertext, i) #calculate IC
        ICdict[i] = IC #store i:IC to the ICdict
    ICdict = sorted(ICdict.items(), key=lambda item:item[1], reverse=True) #sort ICdict with IC in order big to small
    top = [] #store the key length of top n IC
    print(ICdict)
    for i in range(n):
        top.append(ICdict[i][0])

    return top

'''
hack the given file 
question 3 
'''
def crackPassword():
    #open file 
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, './password_protected.txt')
    f = open(file_path)
    ciphertext = f.read()
    f.close()

    #get key 
    key = hackVigenere(ciphertext)
    decipherText = vigenereCipher.decryptMessage(key, ciphertext)
    print(decipherText)
'''
cited from vigHacker.py
'''
def getNthSubkeysLetters(nth, keyLength, message):
    # Returns every nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

    # Use a regular expression to remove non-letters from the message:
    message = message.upper()
    NONLETTERS_PATTERN = re.compile('[^A-Z]')
    message = NONLETTERS_PATTERN.sub('', message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)


def main():
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    key_len = 5
    a = vigenereKeySolver(ciphertext, key_len)
    print(a)
    crackPassword()

if __name__ == "__main__":
    main()