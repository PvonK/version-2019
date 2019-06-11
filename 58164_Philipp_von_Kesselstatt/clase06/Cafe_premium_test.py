import unittest

from Cafe import Premium

# coffee.imputuser(Pago, cantidad de azucar, cantidad de leche) 
# determina el tipo de cafe que se le pide a la maquina

# coffee.sensores(Cantidad de plata, cantidad de agua, cantidad de azucar, cantidad de leche, sensor del vaso)
# determina el estado de la maquina antes de hacer el cafe

class TestCafe(unittest.TestCase):
    def test_cafe_1(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '0')
        coffee.sensores(0, 500, 100, 10, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'Cafe hecho')

    def test_cafe_2(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '0')
        coffee.sensores(0, 500, 100, 4, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'No hay azucar')

    def test_cafe_3(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '0')
        coffee.sensores(0, 500, 100, 10, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'Cafe hecho')

    def test_cafe_4(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '0')
        coffee.sensores(0, 200, 5, 10, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'No hay cafe')

    def test_cafe_5(self):
        coffee = Premium()
        coffee.inputuser ('0', '5', '0')
        coffee.sensores(0, 50, 300, 10, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'Ingrese $50')

    def test_cafe_6(self):
        coffee = Premium()
        coffee.haciendoCafe = True
        self.assertEqual(coffee.HacerCafe(), 'Por favor espere')


    def test_cafe_7(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '0')
        coffee.sensores(0, 20, 150, 10, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'No hay agua')

    def test_cafe_8(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '10')
        coffee.sensores(0, 200, 150, 10, 0, True)
        self.assertEqual(coffee.HacerCafe(), 'No hay leche')

    def test_cafe_9(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '10')
        coffee.sensores(0, 200, 150, 10, 20, True)
        self.assertEqual(coffee.HacerCafe(), 'Cafe hecho')

    def test_cafe_10(self):
        coffee = Premium()
        coffee.inputuser ('50', '5', '0')
        coffee.sensores(0, 200, 150, 10, 0, False)
        self.assertEqual(coffee.HacerCafe(), 'No hay vaso')

if __name__ == '__main__':
    unittest.main()