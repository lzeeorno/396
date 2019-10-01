import math

def lcg(a, b, m, r0):
#R(i+1) = (aR(i)+b) mod(m)
    Rlist = [0,0,0,0,0,0,0,0,0,0]
    R = r0;
    for i in range(len(Rlist)):
        Rlist[i] = (a * R + b) % m
        R = Rlist[i]
    return Rlist

