#reference1:https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

frequency = {"A": 0.0817, "B": 0.015, "C": 0.0278, "D": 0.0425, "E": 0.127,
"F": 0.0222, "G": 0.02, "H": 0.06, "I": 0.0696, "J": 0.00153, "K": 0.00772,
"L": 0.04, "M": 0.024, "N": 0.0674, "O": 0.075, "P": 0.0193, "Q": 0.00095,
"R": 0.0598, "S": 0.0633, "T": 0.091, "U": 0.0275, "V": 0.00978, "W": 0.0236,
"X": 0.0015, "Y": 0.0197, "Z": 0.00074}
frequency_letter = [0.0817, 0.015, 0.0278, 0.0425, 0.127, 0.0222, 0.02, 
0.06, 0.0696, 0.0015, 0.0077, 0.04, 0.024, 0.0675, 0.075, 0.0193, 
0.00095, 0.0598, 0.0633, 0.091, 0.0275, 0.00978, 0.0236, 0.0015, 0.0197, 
0.00074]
ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCV\
    KVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
key_len = 5
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenereKeySolver(ciphertext, key_len):
    ENG_fre = []
    IMC_list = []
    IMC_subList = []
    key_list = []
    splitText = splitingText(ciphertext, 5)
    for i in range(0, key_len):
        # handle each substring independently
        subString = splitText[i]
        frequency_text = countFeq(subString)
        print(frequency_text)
        for j in LETTERS:
            #find the letter corresponding current letter frequency
            current = LETTERS.index(j)
            length = len(LETTERS) #26 characters
            FreqText = [0] * length
            for i in range(0, length-current):
                FreqText[i] = frequency_text[i + current]
            for i in range(length-current, length):
                FreqText[i] = frequency_text[i + current - length]
            #calculating the IMC according to the formula 
            IMC_sum = 0
            for character in range(0, 26):
                IMC_sum += FreqText[character] * frequency_letter[character]
                print(IMC_sum)
            IMC_subList.append(IMC_sum)

        #sort dictorary
        ##reference2:https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
        IMC_dict_unorder = dict(zip(LETTERS, IMC_subList))
        IMC_dict = sorted(IMC_dict_unorder.items(), key=lambda item : item[1], reverse = True)
        IMC_list.append(IMC_dict)
    print(IMC_list)
    #find 10 possible keys 
    for i in range(0, 10):
        max_key = []
        #print(IMC_list)
        for j in range(0, len(IMC_list)):
            max_key.append(IMC_list[j][0][0])
            print(max_key)
        possible_key = ''.join(max_key)
        #print(possible_key)
        key_list.append(possible_key)
        diff = 1
        for i in range(0, len(IMC_list)):
            open_diff = IMC_list[i][0][1] - IMC_list[i][1][1]
            if open_diff < 1:
                diff = open_diff
                diff_index = i
        del(IMC_list[diff_index][0])
    return key_list

        
            
def splitingText(ciphertext, keylen):
    #spliting Text as some group by the keylength
    keyIndex = 0
    splitText = [""] * keylen
    for i in range(0, len(ciphertext)):
        if ciphertext[i].isalpha():
            character = ciphertext[i].upper()
            if keyIndex >= keylen:
                keyIndex = 0
            splitText[keyIndex] += character
            keyIndex += 1
    # print(splitText[0])
    print(splitText)
    return splitText      


def countFeq(splitText):
    IMC_list = []*(len(splitText)*26)
    #calculate frequency of each letter in the each sunString
    letter_fre = [0] * 26
    letter_len = 0
    for i in range(len(splitText)):
        current_letter_index = LETTERS.index(splitText[i])
        letter_fre[current_letter_index] += 1
        letter_len += 1

    # calculate the frequencies of each letters in current substring
    letter_fre = [letter / letter_len for letter in letter_fre]
    print(letter_fre)
    return letter_fre
  
    
# def findmaxIMC(IMC_list):
#     print(IMC_list)
#     key_1 = []
#     key_2 = []
#     key_3 = []
#     key_4 = []
#     key_5 = []
#     max_IMC = 0
#     sec_IMC = 0
#     p1 = 0
#     p2 = 0
#     # each substring have 26 IMC value
#     # each substring have 26 character
#     for p in range(0, 26):
#         if IMC_list[p] > max_IMC:
#             max_IMC = IMC_list[p]
#             p1 = p
#     key_1.append(p1)
#     for p in range(0, 26):
#         if IMC_list[p] > sec_IMC:
#             if p not in key_1:
#                 sec_IMC = IMC_list[p]
#                 p2 = p
#     key_1.append(p2)
#     # renew the parameters
#     max_IMC = 0
#     sec_IMC = 0
#     p1 = 0
#     p2 = 0
#     # after searched each substring, record positions of first 2 most
#     # possible IMC value    
#     for p in range(26, 52):
#         if IMC_list[p] > max_IMC:
#             max_IMC = IMC_list[p]
#             p1 = p
#     key_2.append(p1)
#     for p in range(26, 52):
#         if IMC_list[p] > sec_IMC:
#             if p not in key_2:
#                 sec_IMC = IMC_list[p]
#                 p2 = p
#     key_2.append(p2)
#     # renew the parameters
#     max_IMC = 0
#     sec_IMC = 0
#     p1 = 0
#     p2 = 0

#     for p in range(52, 78):
#         if IMC_list[p] > max_IMC:
#             max_IMC = IMC_list[p]
#             p1 = p
#     key_3.append(p1)
#     for p in range(52, 78):
#         if IMC_list[p] > sec_IMC:
#             if p not in key_3:
#                 sec_IMC = IMC_list[p]
#                 p2 = p
#     key_3.append(p2)
#     # renew the parameters
#     max_IMC = 0
#     sec_IMC = 0
#     p1 = 0
#     p2 = 0

#     for p in range(78, 104):
#         if IMC_list[p] > max_IMC:
#             max_IMC = IMC_list[p]
#             p1 = p
#     key_4.append(p1)
#     for p in range(78, 104):
#         if IMC_list[p] > sec_IMC:
#             if p not in key_4:
#                 sec_IMC = IMC_list[p]
#                 p2 = p
#     key_4.append(p2)
#     # renew the parameters
#     max_IMC = 0
#     sec_IMC = 0
#     p1 = 0
#     p2 = 0

#     for p in range(104, 130):
#         if IMC_list[p] > max_IMC:
#             max_IMC = IMC_list[p]
#             p1 = p
#     key_5.append(p1)
#     for p in range(104, 130):
#         if IMC_list[p] > sec_IMC:
#             if p not in key_5:
#                 sec_IMC = IMC_list[p]
#                 p2 = p
#     key_5.append(p2)

#     return key_1, key_2, key_3, key_4, key_5


def main():
    a = vigenereKeySolver(ciphertext, key_len)
    print(a)

if __name__ == "__main__":
    main()
