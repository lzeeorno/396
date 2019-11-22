
#hack RSA, caluclate the p,q,d in order by given t,n,e


def finitePrimeHack(t, n, e):
    res_list = []
    # find p & q
    for i in range(2, t):
        if n % i == 0:
            p = i
    q = n//p

    res_list.append(p)
    res_list.append(q)
    #sort the list as p <= q
    res_list.sort()
    # find the d which is modular inverse of e
    d = 0
    y = 1
    far = (p-1)*(q-1)
    while (((far * y) + 1) % e) != 0:
        y += 1
    d = (far * y + 1) // e
    res_list.append(d)
    # print(res_list)
    return res_list


def blockSizeHack(blocks, n, e):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    string = []
    p = 0
    q = 0
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n//p
            break
    x = (p-1)*(q-1)
    y = 1
    d = 0
    while (((x * y) + 1) % e) != 0:
        y += 1
    d = (x * y + 1) // e
    for i in range(len(blocks)):
        blockInt = pow(blocks[i], d, n)
        if blockInt < len(SYMBOLS)**i and blockInt != 0:
            blockInt = blockInt % (len(SYMBOLS)**i)
        else:
            blockInt = blockInt // (len(SYMBOLS)**i)
        string.append(SYMBOLS[blockInt])
    return ''.join(string)


def main():
    # # question1
    t = 100
    n = 493
    e = 5
    print(finitePrimeHack(t, n, e))
    # question3
    blocks = [2361958428825, 564784031984, 693733403745, 693733403745,
                2246930915779, 1969885380643]
    n = 3328101456763
    e = 1827871
    print(blockSizeHack(blocks, n, e))


if __name__ == "__main__":
    main()
