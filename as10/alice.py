from bob import make_bob, otp_encrypt, otp_decrypt
import random
from random import choice

FILTERS="x+"
DIAGONAL="↗↖"
RECTILINEAR="↑→"
ALL=DIAGONAL+RECTILINEAR

def problem1(bob, message):
    """
    An example of quantum key exchange and OTP message sending
    All photons arrive at bob and there is no eavesdropping on the line
    """
    """
    1.  Generate a sufficiently large random key; the key must be at least 5
        times the length of the message and on average half of bobs guess
        filters will be wrong
    2.  Get the filters bob used by using bob.quantum_channel(data)
    3.  Create the list of correct filters sent and figure out which filters
        Bob used correctly
    4.  Tell Bob which filters he guessed incorrectly and should remove
    5.  Create the key and to make sure it's >= 5*len(message) and shorten the
        key to 5*len(message) if it is currently longer
    6.  Call otp_encrypt(key, message) to encrypt the message and then use
        bob.message(ciphertext) to send Bob the coded message
    """
    key = []
    correct_filter = []
    # increase the key as 20 times the length of message
    for i in range(20*len(message)):
        #random create photons 
        random_arrow = random.randint(0,3)
        if random_arrow <= 1:
            # photons is diagonal
            correct_filter.append(FILTERS[0])
        else:
            # photons is rectlinear
            correct_filter.append(FILTERS[1])
        # store all alice key
        key.append(ALL[random_arrow])
    # give alice key to bob
    bob_guess = bob.quantum_channel(key)
    #print(bob.debug())
    T_F = []
    # compare bob's filter and alice's filter 
    for i in range(len(correct_filter)):
        if bob_guess[i] != correct_filter[i]:
            key[i] = ''
            T_F.append(False)
        else:
            T_F.append(True)
    # drop incorrect elements 
    bob.dispose(T_F)
    key = ''.join(key)
    if len(key) > 5*len(message):
        key = key[:5*len(message)]
    else:
        print('key length is not enough')
    ciphertext = otp_encrypt(key, message)
    deciphertext = otp_decrypt(key, ciphertext)
    bob.message(ciphertext)


def problem2(bob, message):
    """
    If Bob selects the incorrect filter, there is a 10% chance that the photon will be lost
    The length of the list of filters returned by Bob is the number of photons that reached bob successfully
    """
    key = []
    correct_filter = []
    for i in range(20*len(message)):
        random_arrow = random.randint(0,3)
        if random_arrow <= 1:
            correct_filter.append(FILTERS[0])
        else:
            correct_filter.append(FILTERS[1])
        key.append(ALL[random_arrow])
    bob_guess = bob.quantum_channel(key)
    #print(bob.debug())
    T_F = []
    for i in range(len(correct_filter)):
        if bob_guess[i] != correct_filter[i]:
            key[i] = ''
            T_F.append(False)
        else:
            T_F.append(True)
    bob.dispose(T_F)
    key = ''.join(key)
    if len(key) > 5*len(message):
        key = key[:5*len(message)]
    else:
        print('key length is not enough')
    ciphertext = otp_encrypt(key, message)
    deciphertext = otp_decrypt(key, ciphertext)
    bob.message(ciphertext)


def problem3(bob, message):
    """
    Eve may be evesdropping and alter the polarity of photons, but no photons are lost
    """
    key = []
    correct_fil = []
    bob_guess = []
    check_list = []
    is_evesdropping = False
    for i in range(30*len(message)):
        random_arrow = random.randint(0,3)
        check_list.append(choice([True, False]))
        if random_arrow <= 1:
            correct_fil.append(FILTERS[0])
        else:
            correct_fil.append(FILTERS[1])
        key.append(ALL[random_arrow])
    
    bob_guess = bob.quantum_channel(key, check_list)
    print(bob_guess)
    true_false = []
    for i in range(len(correct_fil)):
        if check_list[i] == False:
            if bob_guess[i] != correct_fil[i]:
                key[i] = ""
                true_false.append(False)
            else:
                true_false.append(True)
        else:
            if bob_guess[i] != key[i]:
                if (bob_guess[i] in DIAGONAL and key[i] in DIAGONAL) or (bob_guess[i] in RECTILINEAR and key[i] in RECTILINEAR):
                        is_evesdropping = True    
                        if is_evesdropping == True:
                            bob.report_eve()                
            key[i] = ""
    bob.dispose(true_false)
    key = ''.join(key)
    if len(key) > 5*len(message):
        key = key[0:5*len(message)]
    if key == ''.join(bob.debug()[:5*len(message)]):
        ciphertext = otp_encrypt(key, message)
        bob.message(ciphertext)



def problem4(bob, message):
    """
    Eve may be evesdropping and alter the polarity of photons
    If Eve uses the wrong filter, there is a 10% that the packet will be lost
    If Bob uses the wrong filter, there is a 10% chance that the photon will be lost
    The length of the list of filters returned by Bob is the number of photons that reached bob successfully
    """
    key = []
    correct_fil = []
    bob_guess = []
    check_list = []
    for i in range(30*len(message)):
        random_arrow = random.randint(0,3)
        check_list.append(choice([True, False]))
        if random_arrow <= 1:
            correct_fil.append(FILTERS[0])
        else:
            correct_fil.append(FILTERS[1])
        key.append(ALL[random_arrow])
    
    bob_guess = bob.quantum_channel(key, check_list)
    true_false = []
    for i in range(len(correct_fil)):
        if check_list[i] == False:
            if bob_guess[i] != correct_fil[i]:
                key[i] = ""
                true_false.append(False)
            else:
                true_false.append(True)
        else:
            if bob_guess[i] != key[i] and bob_guess[i] != None:
                if (bob_guess[i] in DIAGONAL and key[i] in DIAGONAL) or (bob_guess[i] in RECTILINEAR and key[i] in RECTILINEAR):
                    bob.report_eve()
                    
            key[i] = ""
    bob.dispose(true_false)
    key = ''.join(key)
    if len(key) > 5*len(message):
        key = key[0:5*len(message)]
    if key == ''.join(bob.debug()[0:5*len(message)]):
        ciphertext = otp_encrypt(key, message)
        bob.message(ciphertext)

def test():
    # problem1(make_bob(problemNumber=1), "HELLO BOB HOW ARE YOU DOING TODAY")
    # problem2(make_bob(problemNumber=2), "HELLO BOB HOW ARE YOU DOING TODAY")
    problem3(make_bob(problemNumber=3), "HELLO BOB HOW ARE YOU DOING TODAY")
    # problem4(make_bob(problemNumber=4), "HELLO BOB HOW ARE YOU DOING TODAY")
    return

if __name__ == "__main__":
    test()
