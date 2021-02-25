import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_Fibonacci(self):
        #Normal tests
        self.assertEqual(fibonacci.fibonacci(0), 0)
        self.assertEqual(fibonacci.fibonacci(1), 1)
        self.assertEqual(fibonacci.fibonacci(2), 1)
        self.assertEqual(fibonacci.fibonacci(3), 2)
        self.assertEqual(fibonacci.fibonacci(4), 3)
        self.assertEqual(fibonacci.fibonacci(9), 34)

        #Negative number
        try:
            fibonacci.fibonacci(-1)
        except:
            pass
        else:
            self.fail("Fibonacci took a negative number")

        #Invalid data type (string)
        try:
            fibonacci.fibonacci("test")
        except:
            pass
        else:
            self.fail("Fibonacci took a string")

        #Invalid data type (double)
        try:
            fibonacci.fibonacci(2.5)
        except:
            pass
        else:
            self.fail("Fibonacci took a negative double")



if __name__ == '__main__':
    unittest.main(verbosity=2)