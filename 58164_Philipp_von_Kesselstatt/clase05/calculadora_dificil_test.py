import unittest

from calc import Dificil

class TestCalc(unittest.TestCase):
    def test_calc_1(self):
        calc = Dificil()
        calc.inputuser('1')
        calc.inputuser('+')
        calc.inputuser('2')
        calc.inputuser('=')
        self.assertEqual(calc.display(), '3')

    def test_calc_2(self):
        calc = Dificil()
        calc.inputuser('1')
        calc.inputuser('-')
        calc.inputuser('1')
        calc.inputuser('=')
        self.assertEqual(calc.display(), '0')
        
    def test_calc_3(self):
        calc = Dificil()
        calc.inputuser('2')
        calc.inputuser('*')
        calc.inputuser('3')
        calc.inputuser('=')
        self.assertEqual(calc.display(), '6')

    def test_calc_4(self):
        calc = Dificil()
        calc.inputuser('1')
        calc.inputuser('5')
        calc.inputuser('/')
        calc.inputuser('3')
        calc.inputuser('=')
        
        self.assertEqual(calc.display(), '5')

    def test_calc_5(self):
        calc = Dificil()
        calc.inputuser('5')
        calc.inputuser('1')
        calc.inputuser('-')
        calc.inputuser('c')

        self.assertEqual(calc.display(), '')

    def test_calc_6(self):
        calc = Dificil()
        calc.inputuser('1')
        calc.inputuser('1')
        calc.inputuser('+')
        calc.inputuser('1')
        calc.inputuser('1')
        calc.inputuser('=')

        self.assertEqual(calc.display(), '22')

    def test_calc_7(self):
        calc = Dificil()
        calc.inputuser('4')
        calc.inputuser('1')
        calc.inputuser('+')
        calc.inputuser('3')
        calc.inputuser('-')
        calc.inputuser('2')
        calc.inputuser('=')

        self.assertEqual(calc.display(), '42')


    def test_calc_8(self):
        calc = Dificil()
        calc.inputuser('4')
        calc.inputuser('1')
        calc.inputuser('+')
        calc.inputuser('3')
        calc.inputuser('-')
        calc.inputuser('2')
        calc.inputuser('*')
        calc.inputuser('1')
        calc.inputuser('1')
        calc.inputuser('+')
        calc.inputuser('3')
        calc.inputuser('=')
        
        self.assertEqual(calc.display(), '25')

    def test_calc_9(self):
        calc = Dificil()
        calc.inputuser('1')
        calc.inputuser('5')
        calc.inputuser('+')
        calc.inputuser('3')
        calc.inputuser('*')
        calc.inputuser('3')
        calc.inputuser('*')
        calc.inputuser('3')
        calc.inputuser('3')
        calc.inputuser('/')
        calc.inputuser('3')
        calc.inputuser('-')
        calc.inputuser('5')
        calc.inputuser('=')
        
        self.assertEqual(calc.display(), '109')
        


if __name__ == '__main__':
    unittest.main()