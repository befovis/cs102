import unittest
from src.lab1 import calculator

class CalculatorTestCase(unittest.TestCase):
    def test_check_operation(self):
        self.assertTrue(calculator.check_operation(["123", "456"]))
        self.assertTrue(calculator.check_operation(["789", "12.3"]))
        self.assertTrue(calculator.check_operation(["4.56", "78.9"]))
        self.assertTrue(calculator.check_operation(["1.23", "45.6"]))
        self.assertFalse(calculator.check_operation(["abc", "456"]))
        self.assertFalse(calculator.check_operation([".12", "45"]))
        self.assertFalse(calculator.check_operation(["12.", ""]))
        self.assertFalse(calculator.check_operation(["qwerty", "asdfg"]))
        self.assertFalse(calculator.check_operation(["0.000.0", "123"]))

    def test_formatting_expression(self):
        self.assertEquals(calculator.formatting_expression("123.456"), "123456")
        self.assertEquals(calculator.formatting_expression("123"), "123")
        self.assertEquals(calculator.formatting_expression("123."), "f")
        self.assertEquals(calculator.formatting_expression(".123"), "f")
        self.assertEquals(calculator.formatting_expression("12.34.56"), "f")

    def test_formatting_result(self):
        self.assertEquals(calculator.formatting_result("10.0"), "10")
        self.assertEquals(calculator.formatting_result("0.0"), "0")
        self.assertEquals(calculator.formatting_result("0.00001"), "0.00001")
        self.assertEquals(calculator.formatting_result("123.456"), "123.456")

    def test_calculating(self):
        self.assertEquals(calculator.calculating("3+3", "+"), 6.0)
        self.assertEquals(calculator.calculating("+++", "+"), "f")
        self.assertEquals(calculator.calculating("ma+sk", "+"), "f")
        self.assertEquals(calculator.calculating("12.345+56.789", "+"), 69.134)
        self.assertEquals(calculator.calculating("n*9", "*"), "f")
        self.assertEquals(calculator.calculating("7*9", "*"), 63.0)
        self.assertEquals(calculator.calculating("1.2*0.5", "*"), 0.6)
        self.assertEquals(calculator.calculating("0/5", "/"), 0.0)
        self.assertEquals(calculator.calculating("5/0", "/"), "zero")
        self.assertEquals(calculator.calculating("45/45", "/"), 1.0)
        self.assertEquals(calculator.calculating("+-/", "-"), "f")
        self.assertEquals(calculator.calculating("34-34", "-"), 0.0)
        self.assertEquals(calculator.calculating("3+3*3", "+"), 12)
        self.assertEquals(calculator.calculating("3+(-4)", "+"), -1)

    if __name__ == '__main__':
        unittest.main()