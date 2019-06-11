class Calculadora (object):

    def __init__ (self):

        self.ingresando = True
        
        self.acumulador = ''
        self.regb = '0'
        self.operando = ''


    def ingresar(self, usuario):


        try:
            int(usuario)
            if self.operando == '':
                self.acumulador += usuario
            else:
                self.regb += usuario
        except:            
                
            
            if usuario == '=' or (self.operando != '' and self.regb != ''):
                if self.operando == '+':
                    self.acumulador = str(  int(   int(self.acumulador) + int(self.regb) ) )
                    
                if self.operando == '-':
                    self.acumulador = str(  int(   int(self.acumulador) - int(self.regb) ) )                  

                if self.operando == '*':
                    self.acumulador = str(  int(  int(self.acumulador) * int(self.regb)  ) )                    

                if self.operando == '/':
                    self.acumulador = str(  int(  int(self.acumulador) / int(self.regb) ) )
                
                self.regb = ''
                self.operando = ''    

                if usuario != '=':
                    self.operando = usuario
            
            elif usuario == 'c':
                self.acumulador = ''
                self.regb = ''
                self.operando = ''

            else:
                self.operando = usuario
                

                
    
    def display (self):

        display = self.acumulador + self.operando + self.regb

        return display

class Dificil (Calculadora):

    def __init__ (self):

        super().__init__()       
        self.user = ''
        self.sumas = ''
        self.listaop = list()
        self.cantop = 0
        self.antnum = False
        self.listaTerminos = list()

    def inputuser(self, inputteclado):

        self.user += inputteclado

    def display(self):
        
        if self.user.endswith('='):

            for letter in self.user:

                try:
                    int(letter)
                    if self.antnum:
                        self.listaTerminos[self.cantop] += letter
                        self.antnum = True
                    else:
                        self.listaTerminos.append(letter)
                        self.antnum = True
                except:                          
                    if letter == '*' or letter == '/':
                        self.listaTerminos[self.cantop] += letter
                        self.antnum = True
                    
                    elif letter == '+' or letter == '-' or letter == '=':
                        self.listaTerminos[self.cantop] += '='
                        self.listaop.append(letter)
                        self.cantop+=1
                        self.antnum = False 

            return self.calculos()

        elif self.user.endswith('c'):
            
            self.ingresar('c')
            self.sumas = ''
            self.listaop = list()
            self.cantop = 0
            self.antnum = False
            self.listaTerminos = list()
            return ''
        else:
            return self.user

    def calculos (self):

        for num in range(self.cantop):    
            for letter in self.listaTerminos[num]:

                self.ingresar(letter)

            self.sumas += self.acumulador + self.listaop[num]
            self.ingresar('c')
        
        for letter in self.sumas:

            self.ingresar(letter)

        return self.acumulador



            



    