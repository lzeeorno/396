
def crack_lcg(m, r1, r2, r3):
    x = 0;
    abList = [0,0]
    inverse = (r3-r2) % m
    a_coefficient = r2 - r1
    if a_coefficient == 0:
        return abList
    while((m*x + inverse) % a_coefficient != 0):
        x += 1
    a = (m*x + inverse) / a_coefficient
    x = 0

    while(m*x + r3 - a*r2 <0):
        x += 1
    b = m*x + r3 - a*r2

    abList[0] = a
    abList[1] = b

    return abList
