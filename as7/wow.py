import vigenereCipher

ENG_LETT_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 
'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 
'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 
'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenereKeySolver(ciphertext, key_len):

    keyIndex = 0
    splitText = [""] * key_len
    for i in range(0, len(ciphertext)):
        if ciphertext[i].isalpha():
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

        for possible_key in LETTERS:
            deciphered_subString = vigenereCipher.decryptMessage(possible_key, subString)

            count_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

            for index in range(0, len(deciphered_subString)):
                current_letter = deciphered_subString[index]
                count_dict[current_letter] = count_dict[current_letter] + 1

            imc = 0
            for letter in count_dict:
                t_value = count_dict[letter] / len(deciphered_subString)
                e_value = ENG_LETT_FREQ[letter] / 100
                imc += t_value * e_value

            key_imc_tuple = (possible_key, imc)
            imc_subString.append(key_imc_tuple)

        for n in range(0, len(imc_subString)):
            for m in range(len(imc_subString)-1, n, -1):
                if imc_subString[m-1][1] < imc_subString[m][1]:
                    imc_subString[m], imc_subString[m-1] = imc_subString[m-1], imc_subString[m]

        imc_list.append(imc_subString)

    keys_list = []
    for i in range(0, 10):
        current_key = ""
        for m in range(0, key_len):
            current_key = current_key + imc_list[m][0][0]
        keys_list.append(current_key)

        min_difference = float(imc_list[0][0][1])
        for i in range(0, key_len):
            current_difference = imc_list[i][0][1] - imc_list[i][1][1]
            if current_difference < min_difference:
                min_difference_index = i
                min_difference = current_difference

        del(imc_list[min_difference_index][0])

    return keys_list

def main():
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    key_len = 5
    a = vigenereKeySolver(ciphertext, key_len)
    print(a)

if __name__ == "__main__":
    main()