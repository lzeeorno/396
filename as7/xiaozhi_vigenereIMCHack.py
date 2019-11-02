import sys, re
# import vigenereCipher, detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_freq = [0.0817, 0.0129, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 0.0010, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

def vigenereKeySolver(ciphertext, keylength):

    splited_text_list = split_text(ciphertext, keylength)

    IMC_list = []

    # already know the keylength
    # split the ciphertext into substing
    # there are # keylength substrings
    # for each substring:
    for i in range(keylength):

        current_string = splited_text_list[i]

        letter_freq_text = calculate_freq(current_string)

        IMC_substring = []

        # for current substring
        # there are 26 possible keys
        for current_key in LETTERS:
            current_letter_freq_text = decrypt_substring(letter_freq_text, current_key)
            #print(current_letter_freq_text)
            # calculate the IMC with current substring and current key
            IMC_sum = 0
            for letter in range(len(LETTERS)):
                IMC_sum += current_letter_freq_text[letter] * letter_freq[letter]
                print(IMC_sum)
            IMC_substring.append(IMC_sum)
        #print(IMC_substring)
        # sort the IMC list
        IMC_subsring_dict = dict(zip(LETTERS, IMC_substring))
        IMC_subsring_sorted = sorted(IMC_subsring_dict.items(), key=lambda item:item[1], reverse=True)
        IMC_list.append(IMC_subsring_sorted)
        #print(IMC_subsring_sorted)

    print(len(IMC_list))

    # possible keys sorted by the decreasing order
    key_list = []

    for i in range(10):
        # maximum IMC must be the sum of maximum IMC for each substring
        # i.e. the first key of each IMC_substring_sorted
        maxIMC_key = get_current_key(IMC_list)
        key_list.append(maxIMC_key)
        #print(key_list)
        # the next maximum IMC
        # replace one IMC_substring which with minimum difference with next_key
        # delete the ole one to make the next_key become the first key
        min_diff_index = calculate_min_difference(IMC_list)
        del(IMC_list[min_diff_index][0])

    return key_list

def split_text(text, keylength):
    current_index_Key = 0
    splited_text = [""] * keylength
    for i in range(len(text)):
        # should work on the full set of ASCII char- acters
        if text[i].isalpha():
            # not be case-sensitive
            current_symbol = text[i].upper()
            # recycle with key length
            if current_index_Key >= keylength:
                current_index_Key = 0
            splited_text[current_index_Key] += current_symbol
            current_index_Key += 1

    return splited_text

def calculate_freq(string):
    #print(string)
    letter_count = [0] * len(LETTERS)
    letter_total = 0

    # count the number of each letters in currunt substring
    for j in range(len(string)):
        current_letter_index = LETTERS.index(string[j])
        letter_count[current_letter_index] += 1
        letter_total += 1
    #print(letter_total)
    # calculate the frequencies of each letters in current substring
    letter_count = [letter / letter_total for letter in letter_count]
    print(letter_count)
    return letter_count

def decrypt_substring(letter_count, key):
    current_key = LETTERS.index(key)
    total_key = len(LETTERS)
    decrypted_letter_count = [0] * total_key

    for i in range (total_key - current_key):
        decrypted_letter_count[i] = letter_count[i + current_key]
    for i in range (total_key - current_key, total_key):
        decrypted_letter_count[i] = letter_count[i + current_key - total_key]

    return decrypted_letter_count

# first keys for each substring
# the sum of IMC is maximum
def get_current_key(IMC_list):
    print(IMC_list)
    maxIMC_key_list = []
    for i in range(len(IMC_list)):
        maxIMC_key_list.append(IMC_list[i][0][0])
    maxIMC_key = ''.join(maxIMC_key_list)
    #print(maxIMC_key)
    return maxIMC_key

def calculate_min_difference(IMC_list):
    # the upper bond of IMC is 1 and all IMC must be positive
    # so the difference must be less than 1
    # it is safe to set min_diff as 1
    min_diff = 1
    for i in range(len(IMC_list)):
        current_diff = IMC_list[i][0][1] - IMC_list[i][1][1]
        if current_diff < min_diff:
            min_diff = current_diff
            min_diff_index = i
    return min_diff_index

'''
For Problem 2
'''

# def hackVigenere(ciphertext):
#     # get 5 most possible keylength
#     possible_key_length = keyLengthIC(ciphertext, 5)

#     max_acc = 0

#     for key_length in possible_key_length:
#         # get 10 most possible keys
#         possible_keys = vigenereKeySolver(ciphertext, key_length)

#         for key in possible_keys:
#             decrpted_text = vigenereCipher.decryptMessage(key, ciphertext)
#             current_acc = detectEnglish.getEnglishCount(decrpted_text)
#             # check whether the current key is the best one
#             if current_acc > max_acc:
#                 max_acc = current_acc
#                 best_key = key

#     return best_key

# '''
# Copy from Assignment 6 Problem 4
# '''

# def stringIC(inputstr):

#     count_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
#     letter_count = 0
#     for i in range(len(inputstr)):
#         if inputstr[i].isalpha():
#             current_symbol = inputstr[i].upper()
#             count_dict[current_symbol] += 1
#             letter_count += 1

#     if letter_count < 2:
#         print("Please input longer message.")
#         sys.exit()

#     numerator_sum = 0
#     for letter in count_dict:
#         numerator_sum += count_dict[letter] * (count_dict[letter] - 1)
#     denominator = letter_count * (letter_count - 1)

#     indexofCoincidence = numerator_sum / denominator
#     return indexofCoincidence

# def subseqIC(ciphertext, keylen):
#     ic_sum = 0
#     for i in range(1, keylen + 1):
#         message = getNthSubkeysLetters(i, keylen, ciphertext)
#         ic = stringIC(message)
#         ic_sum += ic
#     ic_avg = ic_sum / keylen
#     return ic_avg

# def getNthSubkeysLetters(nth, keyLength, message):
#     # Returns every nth letter for each keyLength set of letters in text.
#     # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
#     #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
#     #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
#     #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

#     # Use a regular expression to remove non-letters from the message:
#     message = message.upper()
#     NONLETTERS_PATTERN = re.compile('[^A-Z]')
#     message = NONLETTERS_PATTERN.sub('', message)

#     i = nth - 1
#     letters = []
#     while i < len(message):
#         letters.append(message[i])
#         i += keyLength
#     return ''.join(letters)

# def keyLengthIC(ciphertext, n):
#     key_lengths = list(range(10))
#     key_lengths = [i + 1 for i in key_lengths]
#     ic_list = []
#     for i in range(1, 11):
#         ic = subseqIC(ciphertext, i)
#         ic_list.append(ic)
#     ic_index = dict(zip(key_lengths, ic_list))
#     ic_sorted = sorted(ic_index.items(), key=lambda item:item[1], reverse=True)

#     target_length = []
#     for i in range(n):
#         target_length.append(ic_sorted[i][0])
#     return target_length

# '''
# Problem 3
# '''

# def crackPassword():
#     # read text from the file
#     input_file = open("password_protected.txt")
#     ciphered_message = input_file.read()
#     input_file.close()

#     # get the most possible key
#     guess_key = hackVigenere(ciphered_message)
#     deciphered_text = vigenereCipher.decryptMessage(guess_key, ciphered_message)

#     # output the result in a file
#     output_file = open("a7.txt", "w")
#     output_file.write(deciphered_text)
#     output_file.close()

#     print(deciphered_text)

def main():
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCV\ KVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    a = vigenereKeySolver(ciphertext, 5)
    print(a)

# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()