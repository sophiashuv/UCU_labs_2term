import unittest
from vigenere_cipher import *


class TestStringMethods(unittest.TestCase):

    def test_extend_keyword(self):
        cipher = VigenereCipher("START")
        self.assertEqual(cipher.extend_keyword(20), "STARTSTARTSTARTSTART")

    def test_combine_character(self):
        self.assertEqual(combine_character("M", "S"), "E")
        self.assertEqual(combine_character("N", "S"), "F")
        self.assertEqual(combine_character("n", "s"), "F")


    def test_separate_character(self):
        self.assertEqual(separate_character("M", "S"), "U")
        self.assertEqual(separate_character("N", "S"), "V")
        self.assertEqual(separate_character("n", "s"), "V")

    def test_encode(self):
        cipher = VigenereCipher("START")
        self.assertEqual(cipher.encode("HELLO"), "ZXLCH")

    def test_decode(self):
        cipher = VigenereCipher("START")
        self.assertEqual(cipher.decode("ZWDDG"), "HDDMN")

    def test_encode_register(self):
        cipher = VigenereCipher("Start")
        self.assertEqual(cipher.encode("Hello"), "ZXLCH")
        cipher = VigenereCipher("StArt")
        self.assertEqual(cipher.encode("HelLo"), "ZXLCH")
        cipher = VigenereCipher("START")
        self.assertEqual(cipher.encode("helLo"), "ZXLCH")

    def test_encode_character(self):
        cipher = VigenereCipher("S")
        self.assertEqual(cipher.encode("H"), "Z")
        cipher = VigenereCipher("START")
        self.assertEqual(cipher.encode("h"), "Z")
        cipher = VigenereCipher("S")
        self.assertEqual(cipher.encode("HELLO"), "ZWDDG")

    def test_encode_spaces(self):
        cipher = VigenereCipher("STERT ENCODING")
        self.assertEqual(cipher.encode("HELLO WORLD"), "ZXPCHPSENR")
        cipher = VigenereCipher("START")
        self.assertEqual(cipher.encode("HELLO WORLD"), "ZXLCHOHRCW")
        cipher = VigenereCipher("STERT ENCODING")
        self.assertEqual(cipher.encode("HELLO"), "ZXPCH")


if __name__ == '__main__':
    unittest.main()