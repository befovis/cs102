import unittest
from src.lab2 import rsa

class RsaTestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(rsa.is_prime(33))
        self.assertTrue(rsa.is_prime(61))
        self.assertFalse(rsa.is_prime(63))
        self.assertFalse(rsa.is_prime(77))
        self.assertTrue(rsa.is_prime(79))
        self.assertTrue(rsa.is_prime(103))

    def test_gcd(self):
        self.assertEquals(rsa.gcd(25, 77), 1)
        self.assertEquals(rsa.gcd(21, 35), 7)
        self.assertEquals(rsa.gcd(660, 66), 66)
    def test_multiplicative_inverse(self):
        self.assertEquals(rsa.multiplicative_inverse(7, 47), 27)
        self.assertEquals(rsa.multiplicative_inverse(7, 51), 22)
        self.assertEquals(rsa.multiplicative_inverse(7, 60), 43)

    if __name__ == '__main__':
        unittest.main()