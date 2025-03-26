import unittest
from src.lab2 import caesar

class CaesarTestCase(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEquals(caesar.encrypt_caesar(""), "")
        self.assertEquals(caesar.encrypt_caesar("Hello World!", 15), "Wtaad Ldgas!")
        self.assertEquals(caesar.encrypt_caesar("абвг", 15), "абвг")
        self.assertEquals(caesar.encrypt_caesar("12323242-!.", 15), "12323242-!.")

    def test_decrypt_caesar(self):
        self.assertEquals(caesar.decrypt_caesar(""), "")
        self.assertEquals(caesar.decrypt_caesar("Wtaad Ldgas!", 15), "Hello World!")
        self.assertEquals(caesar.decrypt_caesar("абвг", 15), "абвг")
        self.assertEquals(caesar.decrypt_caesar("12323242-!.", 15), "12323242-!.")


    if __name__ == '__main__':
        unittest.main()