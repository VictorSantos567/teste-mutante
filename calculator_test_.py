import unittest

from calculator import calculator_option

class TestMethod(unittest.TestCase):

    def test_sum(self):
        self.assertEquals(calculator_option('+',2,2), 4, "Precisa ser 4")

    def test_subtraction(self):
        self.assertEquals(calculator_option('-',4,2), 2, "Precisar ser 2")

    def test_multiplication(self):
        self.assertEquals(calculator_option('*',3,3), 9,"Precisa ser 9")

    def test_division(self):
        self.assertEquals(calculator_option('/',15,5), 3.0,"Precisar ser 3")
          
    
if __name__ == '__main__':
    unittest.main()