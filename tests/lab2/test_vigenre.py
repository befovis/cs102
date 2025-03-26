import string
import unittest
import random
from src.lab2 import vigenre


class VigenreTestCase(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEquals(vigenre.encrypt_vigenere("", ""), "")
        self.assertEquals(vigenre.encrypt_vigenere("Hello, world!", "Schiller"),"Zgstz, hsidf!")
        self.assertEquals(vigenre.encrypt_vigenere("1234", "A"), "1234")

    def test_decrypt_vigenere(self):
        self.assertEquals(vigenre.decrypt_vigenere("", ""), "")
        self.assertEquals(vigenre.decrypt_vigenere("Zgstz, hsidf!", "Schiller"),"Hello, world!")
        self.assertEquals(vigenre.decrypt_vigenere("1234", "a"), "1234")
        self.assertEquals(vigenre.decrypt_vigenere("abcd", "123"), "abcd")

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = vigenre.encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, vigenre.decrypt_vigenere(ciphertext, keyword))

    if __name__ == '__main__':
        unittest.main()