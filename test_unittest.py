import unittest
from app import app 

class TestPrimeNumber(unittest.TestCase):
    def test_prime_numbers(self):
        prime = app.is_prime(17)
        self.assertTrue(prime, 'True')
        prime = app.is_prime(13219)
        self.assertTrue(prime, 'True')

    def non_prime_number(self):
        non_prime = app.is_prime(36)
        self.assertFalse(non_prime, 'False')
       

        

if __name__ == '__main__':
    unittest.main()