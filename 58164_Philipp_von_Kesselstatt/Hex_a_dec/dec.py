def deca (n):

    d = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    s = ''
    r = 0

    for l in n:
        if l in d:            
            s += str(int(d[l]/8)) + str(int(d[l]/4)%2) + str((int(d[l]/2)%2)) + str(d[l]%2)
        else:            
            s += str(int(int(l)/8)) + str(int(int(l)/4)%2) + str(int(int(l)/2)%2) + str(int(l)%2)

    c = len(s)
    for b in s:
        c-= 1
        r += int(b)*(2**c)

    return r
