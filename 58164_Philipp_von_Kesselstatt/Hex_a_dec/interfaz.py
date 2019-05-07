from dec import deca

def interfaz (n):

    d = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15, 'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

    if not n:
        return 'ingrese un numero'

    try:
        if int(n) < 0:
            return 'ingrese un numero hexadecimal positivo'
        else:     
            return deca(n)
    except:
        for l in n:
            if not l in d:
                try:
                    int(l)
                except:
                    return 'el numero debe ser un hexadecimal positivo'
                        
    return deca(n)
       
