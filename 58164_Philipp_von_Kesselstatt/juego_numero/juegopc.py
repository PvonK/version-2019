def juegopc (b,r):

    d ={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

    p = {}

    b = 0
    
    for n in range(10):

        print (n)

        d[str(n)]=int(input(str(n)+str(n)+str(n)+str(n) + '     bien:   '))
        r = input('regular:   ')

        print (d[str(n)])

    for v in d:
        if d[v] == 0:
            f = v
            print(v)
            print (d[v])
            print(f)
        else :
            p[v]=1

    while b !=4:

        for v in d:
            while d[v] > 0:

                #cambiar de lugar
                b += int(input (str(d[v])+str(d[f])+str(d[f])+str(d[f])+ '      bien:   '))
                r = input('regular:   ')
                p[v]='0'


                b += int(input (str(d[f])+str(d[v])+str(d[f])+str(d[f])+ '      bien:   '))
                r = input('regular:   ')
                p[v]='1'

                b += int(input (str(d[f])+str(d[f])+str(d[v])+str(d[f])+ '      bien:   '))
                r = input('regular:   ')
                p[v]='2'

                b += int(input (str(d[f])+str(d[f])+str(d[f])+str(d[v])+ '      bien:   '))
                r = input('regular:   ')
                p[v]='3'

                print(d[v])

                d[v]-=1
                
        
        
        


    return b


    
x=input('aaaaa')
y=input('aaaa')
print(juegopc(x, y))
