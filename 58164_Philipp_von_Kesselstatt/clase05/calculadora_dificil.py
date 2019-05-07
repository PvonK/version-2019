class calculadora (object):

    def __init__ (self):

        self.ingresando = True
        
        self.acumulador = ''
        self.regb = ''
        self.operandos = ''
        self.num = list()
        self.c=0
        self.positionmul = list()
        self.cont = 0        

    def ingresar(self, usuario):   

        for letter in usuario:
        
            try:
                int(letter)
                self.num[self.c] += usuario

                print(self.num[self.c])

            except:
                if usuario == '=':
                    
                    for position in range( len(self.operandos)):

                        if self.operandos[position] == '*':
                            self.num[position] = int (  int(self.num[position]) * int(self.num[position+1])  )

                            self.positionmul[self.cont] = position

                        if self.operandos[position] == '/':
                            self.num[position] = int( int(self.num[position]) / int(self.num[position+1]) )

                            self.positionmul[self.cont] = position

                        self.cont +=1

                    for n in range(len(self.positionmul)):
                        
                        for m in range(1, len(self.positionmul)):
                            self.num[m] = self.num[m+1]

                        for p in self.positionmul:
                            self.operandos[p] = self.operandos[p+1]

                    position = 0
                    for position in range( len(self.operandos)):

                        if self.operandos[position] == '+':
                            self.num[position] = int (  int(self.num[position]) + int(self.num[position+1])  )

                        if self.operandos[position] == '-':
                            self.num[position] = int( int(self.num[position]) - int(self.num[position+1]) )

                                

                        


                        

                else:
                    self.operandos += usuario
                    self.c+=1

        self.c+=1


        
    
    def display (self):

        display = str(self.acumulador + self.operandos + self.regb)

        return display