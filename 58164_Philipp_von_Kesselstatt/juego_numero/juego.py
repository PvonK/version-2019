import random

def juego ():

    #n=str(random.randint(0,9)) + str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

    n= '1914'

    b=0
    r=0
    while b != 4:
        
        b=0
        r=0
        a=input('Ingrese un numero:          ')
        
        for l in range(4):

            if n[l] == a[l]:
                b+=1
            
            
            for c in range(4):
                if n[c]==a[l] and n[l] != a[l]:
                    h = r + 1
                    if h > r:
                        l+=1
                    r+=1
                
            

        print('R',r)
        print('B',b)



    return (a)


print(juego())