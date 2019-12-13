import vigenereHacker
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
    
