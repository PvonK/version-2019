import unittest
from cafecitooo import (
  Cafezote,
  Cafecito)



class TestCafecito(unittest.TestCase):


   def setUp(self):
       self.cafecito = Cafecito(500,50,50,23,0)

   def test_startcoffee_EXITO(self):
       self.assertTrue(self.cafecito.startcoffee(5,True))
       self.assertEqual(self.cafecito.agua, 400)
       self.assertEqual(self.cafecito.cafe, 45)
       self.assertEqual(self.cafecito.azucar, 45)
       self.assertEqual(self.cafecito.moneda, 24)

   def test_startcoffee_no_agua(self):
       self.cafecito.agua = 0
       self.assertFalse(self.cafecito.startcoffee(5,True))
       self.assertEqual(self.cafecito.agua, 0)
       self.assertEqual(self.cafecito.cafe, 50)
       self.assertEqual(self.cafecito.azucar, 50)
       self.assertEqual(self.cafecito.moneda, 23)

   def test_startcoffee_no_cafe(self):
      self.cafecito.cafe = 0
      self.assertFalse(self.cafecito.startcoffee(5,True))
      self.assertEqual(self.cafecito.agua, 500)
      self.assertEqual(self.cafecito.cafe, 0)
      self.assertEqual(self.cafecito.azucar, 50)
      self.assertEqual(self.cafecito.moneda, 23)

   def test_startcoffee_no_azucar(self):
      self.cafecito.azucar = 0
      self.assertFalse(self.cafecito.startcoffee(5,True))
      self.assertEqual(self.cafecito.agua, 500)
      self.assertEqual(self.cafecito.cafe, 50)
      self.assertEqual(self.cafecito.azucar, 0)
      self.assertEqual(self.cafecito.moneda, 23)



#----------------------------------------------------------------------
if __name__ == "__main__":
  unittest.main()