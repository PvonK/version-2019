class Cafezote():

    def __init__(self,agua,cafe,azucar,moneda,leche):
        self.mc = False
        self.agua = agua
        self.cafe = cafe
        self.azucar = azucar
        self.leche = leche
        self.moneda = moneda
        self.az = 0

    def hayTodo(self):
        pass

    def descontar(self):
        pass

    def hacerCafe(self):
        if self.hayTodo():
            self.descontar()

class Cafecito (Cafezote):

    az = input('5g o 0g de azucar? ')
    
    def hayTodo(self):

        if self.money == False:
            return False
        elif self.mc == True:
            return False
        elif self.agua < 100:
            return False
        elif self.cafe < 5:
            return False
        elif self.azucar < self.az:
            return False
        else:
            return True

    def descontar(self):

        self.mc = True
        self.agua -= 100
        self.cafe -= 5
        self.azucar -= self.az
        self.moneda += 1
        self.mc = False
        self.money = False

