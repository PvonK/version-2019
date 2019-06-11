class Basico (object):

    def __init__(self):

        self.haciendoCafe = False

    def sensores (self, Smoney, Sagua, Scafe, Sazucar, Sleche, Svaso):

        self.cantMoney =  Smoney
        self.cantAgua = Sagua
        self.cantCafe = Scafe
        self.cantAzucar = Sazucar 
        self.cantLeche = Sleche
        self.vaso = Svaso
        self.errorMessage = 'Error'

    def HayTodo (self):
        pass

    def Desc (self):
        pass

    def HacerCafe(self):
        if not self.haciendoCafe:
            if self.HayTodo():
                self.Desc()
                return 'Cafe hecho'
            else:
                return self.errorMessage
        else:
            return 'Por favor espere'
                
            
class Cafe (Basico):

    def __init__ (self):

        super().__init__()        
        self.pago = 0
        self.az = 0

    def inputuser (self, pago, conazucar):
        self.pago = int(pago)
        self.az = int(conazucar)

    def HayTodo (self):

        if self.pago != 40:
            self.errorMessage = 'Ingrese $40'
            return False
        elif self.cantAgua < 100:
            self.errorMessage = 'No hay agua'
            return False
        elif self.cantCafe < 100:
            self.errorMessage = 'No hay cafe'
            return False
        elif self.az > self.cantAzucar:
            self.errorMessage = 'No hay azucar'
            return False
        else:
            return True

    def Desc (self):

        self.haciendoCafe = True    
        self.cantMoney += self.pago 
        self.cantAgua -= 100
        self.cantCafe -= 100
        self.cantAzucar -= self.az
        self.haciendoCafe = False

class Premium (Basico):

    def __init__ (self):

        super().__init__()        
        self.pago = 0
        self.az = 0
        self.le = 0

    def inputuser (self, pago, conazucar, conleche):

        self.pago = int(pago)
        self.az = int(conazucar)
        self.le = int(conleche)

    def HayTodo (self):

        if self.pago != 50:
            self.errorMessage = 'Ingrese $50'
            return False
        elif not self.vaso:
            self.errorMessage = 'No hay vaso'
            return False
        elif self.cantAgua < 100 - self.le:
            self.errorMessage = 'No hay agua'
            return False
        elif self.cantCafe < 100:
            self.errorMessage = 'No hay cafe'
            return False
        elif self.az > self.cantAzucar:
            self.errorMessage = 'No hay azucar'
            return False
        elif self.le > self.cantLeche:
            self.errorMessage = 'No hay leche'
            return False
        else:
            return True

    def Desc (self):
        
        self.haciendoCafe = True    
        self.cantMoney += self.pago 
        self.cantAgua -= (100 - self.le)
        self.cantCafe -= 100
        self.cantAzucar -= self.az
        self.cantLeche -= self.le
        self.haciendoCafe = False



