"""
Tasks:
1. Please read the comments first.
2. Please learn how to use guess() and findLetters().
3. You should use different methods to break the cipher. These methods
include frequency analysis, consonant/vowel distinction,
guessing short frequent words, and finally matching partially
deciphered words with regular expressions.
4. Print out the decipherd text.
"""
from subCrack import *

unused = alphabet

'''
TODO:
 Read the text file which contains the ciphertext.
 Read the corpus file wells.text.
'''
#Example
#fileObj = open('ciphers/filename.txt','r')
#Call read() to read a string from your cipher file.

'''
TODO:
 First we use letter frequency analysis. Use the
showLetterFrequency(text) function in subCrack module.
You should apply this function both on your corpus file,
wells.txt, and also the ciphertext to try to match them.
'''

'''
TODO:
You may have to make guesses in every step of
your program and need to replace the letters of your 
guess with some letters in the ciphertext. To do that, you 
can use the guess() from subCrack module. 
****
NOTE that the ciphertext will be all lowercase, while the deciphered text will be all UPPERCASE.
'''
#Example
#(unused,ciphertext) = guess(unused,'xyz','EAO',ciphertext)


'''
TODO:
Next we try consonant/vowel distinction method. 
Use neighborCount(text) to get the neighbor count
dictionary and print it using the showCounts(dict)
function. You have to guess which of the most frequent
letters in your ciphertext are vowels and consonants.
'''
#Example:
#How to read showCounts()'s output?
#E.g. Below is the first row from showCounts()
#   a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  
#a  2  1  0  0  0  0  0  1  0  0  2  0  4  0  0  1  0  0  0  2  0  0  1  0  0  0 	 18
#In ciphertext, letter 'a' encodes an unknown letter.
#'a' is a neighbour of 8 letters:'a','b','h','k','m','p,'t','w'. The numbers(2,1,0,0,0....) are the times 'a' occurs next to that letter.
# Number 18 means that for the other 18 letters, 'a' is not a neighbor.
# Among 26 letters, 'a' is only 8 letters' neighbors.(8 = 26-18).
# So, 'a' might encodes a consonant.


'''
TODO:
Now we have deciphered some letters in the ciphertext.
The next step is to guess the short words in the ciphertext.
Find words that are one, two or three letters
long in your ciphertext and also in the corpus file. Then try
compare the words in the corpus file with your ciphertext and 
guess which the missing letters are in the ciphertext.
Use countWords(text) function to apply word frequency analysis 
on the corpus file and also your ciphertext.
'''



'''
TODO:
So far you have identified some of the correct mappings of
plaintext letters to ciphertext. The next step is to guess
the rest of the mappings from the words in your ciphertext
that are not completely deciphered.
You should use Use findLetters(unused,pattern) function
to find the correct mappings. You can use it many times decipher every word 
that is partially deciphered in your ciphertext.
'''




#Example
#reslist = findLetters(unused,'HpTEm')
#print(reslist)
#(unused,ciphertext) = guess(unused,'pm','OL',ciphertext)
'''
TODO:
Print out the deciphered text.
'''
#print(ciphertext)

