def deca (n):

    d = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    r = 0

    c = len(n)
    for l in n:
        if l in d:            
            c-= 1
            r += int(int(d[l]))*(16**c)
            
        else:            
            c-= 1
            r += int(l)*(16**c)
    return r

x = input('aaaaaaaaaaaa     ')
print(deca(x))