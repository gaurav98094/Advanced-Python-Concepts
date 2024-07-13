import unittest
import practice1 as practice1

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(practice1.add(10,5),15)
        self.assertEqual(practice1.add(10,-5),5)
        self.assertEqual(practice1.add(-10,-5),-15)
    
    def test_substract(self):
        self.assertEqual(practice1.substract(10,5),5)
        self.assertEqual(practice1.substract(10,-5),15)
        self.assertEqual(practice1.substract(-10,-5),-5)
        # self.assertAlmostEqual(result,6,delta=2)
    
    def test_multiply(self):
        self.assertEqual(practice1.multiply(10,5),50)
        self.assertEqual(practice1.multiply(10,-5),-50)
        self.assertEqual(practice1.multiply(-10,-5),50)
    
    def test_divide(self):
        self.assertEqual(practice1.divide(10,5),2)
        self.assertEqual(practice1.divide(10,-5),-2)
        self.assertEqual(practice1.divide(-10,-5),2)
        
        with self.assertRaises(ValueError):
            practice1.divide(10,0)
        self.assertRaises(ValueError,practice1.divide,10,0)

if __name__=='__main__':
    unittest.main()

    