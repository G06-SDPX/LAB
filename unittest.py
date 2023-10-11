import unittest

from app import app

class AppTestCase(unittest.TestCase):

  def test_is_prime_17(self):
    res = app.is_prime(17)
    self.assertEqual(res, 'True')

  def test_is_prime_36(self):
    res = app.is_prime(36)
    self.assertEqual(res, 'False')

  def test_is_prime_13219(self):
    res = app.is_prime(13219)
    self.assertEqual(res, 'True')

if __name__ == "__main__":
    unittest.main()
