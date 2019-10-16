LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def evalFile(f1, f2):
    op = open(f1)
    plain = op.read()
    op.close()
    op = open(f2)
    imperfect = op.read()
    op.close()

    list1 = []
    list2 = []
    for letter in plain:
        if letter.upper() in LETTERS:
            if letter.upper() not in list1:
                list1.append(letter.upper())
    for letter in imperfect:
        if letter.upper() in LETTERS:
            if letter.upper() not in list2:
                list2.append(letter.upper())
    keyAccuaracy = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            keyAccuaracy += 1
    keyAccuaracy = keyAccuaracy/len(list1)

    list1 = []
    list2 = []
    for letter in plain:
        if letter.upper() in LETTERS:
            list1.append(letter.upper())
    for letter in imperfect:
        if letter.upper() in LETTERS:
            list2.append(letter.upper())

    deciphermentAccuracy = 0
    
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            deciphermentAccuracy += 1
    deciphermentAccuracy = deciphermentAccuracy/len(list1)

    return [keyAccuaracy, deciphermentAccuracy]
