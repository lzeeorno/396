import random
def antiKasiski(key, plaintext, chars):
    key_len = len(key)#length of key
    modified_text = []#store characters in plaintext as a list and isert char in this list
    for letter in plaintext:#store characters in plaintext
        modified_text.append(letter)
    print(modified_text)      
    for i in range(len(modified_text)):
        
        same_word = '' #store the word at position n*key_len+(the first letter position of the word that you want find its same word)
        n = 0 
        while(''.join(modified_text[i:i+3]).upper() != same_word.upper() and (i+3)+n*key_len < len(modified_text)):
        #if find same three letters word and the distance between them is n*key_len, break the loop
        #or n*key_len+(the index of first letter of the word) > the length of plaintext, break the loop    
            n += 1
            nonLetter_num = 0 #store number of non_letter characters
            for letter in modified_text[i:i+n*key_len]:
                if letter.isalpha() == False:
                    nonLetter_num+=1
            same_word = ''.join(modified_text[i+n*key_len+nonLetter_num:nonLetter_num+(i+3)+n*key_len])
        
        if same_word.upper() == ''.join(modified_text[i:i+3]).upper():#if same_word == modified_text[i:i+3]:
                                         #insert a random char from chars before the same_word
            modified_text.insert(i+nonLetter_num+n*key_len, chars[random.randint(0,len(chars)-1)])
            
          
    return ''.join(modified_text)   
