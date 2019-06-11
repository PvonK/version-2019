class calculadora (object):

    def __init__ (self):

        self.listan = list()
        self.listaop = list()
        self.cantop = 0

    def inputuser(self, inputteclado):

        self.user += inputteclado

    def display(self):
        
        if self.user.endswith('='):
            return self.calculos()
        elif self.user.endswith('c'):
            return ''
        else:
            return self.user

    def calculos ():

        

        