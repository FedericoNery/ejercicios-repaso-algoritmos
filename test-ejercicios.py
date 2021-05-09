import unittest
from unittest import TestCase
from ejercicio_1 import pluralize
from ejercicio_2 import same_length
from ejercicio_3 import operacion_aritmetica
from ejercicio_4 import sevenBoom
from ejercicio_5 import repeticiones
from ejercicio_6 import combinaciones

class TestPluralize(TestCase):
    def test_pluralize_cows_pig(self):
        self.assertEqual(pluralize(["cow", "pig", "cow", "cow"]), {"cows", "pig"})
    def test_pluralize_tables(self):
        self.assertEqual(pluralize(["table", "table", "table"]), {"tables"})
    def test_pluralize_chair_pencil_arm(self):
        self.assertEqual(pluralize(["chair", "pencil", "arm"]), {"chair", "pencil", "arm"})


class TestSameLength(TestCase):
    def test_same_length(self):
        self.assertTrue(same_length("110011100010"))
    def test_same_length_1(self):
        self.assertFalse(same_length("101010110"))
    def test_same_length_2(self):
        self.assertTrue(same_length("111100001100"))
    def test_same_length_3(self):
        self.assertFalse(same_length("111"))

class TestSevenBoom(TestCase):
    BOOM = "Boom!"
    NO_SE_ENCUENTRA_EL_NUMERO = "No se encuentra el número 7"

    def test_seven_boom_case_1(self):
        self.assertEqual(sevenBoom([1, 2, 3, 4, 5, 6, 7]), self.BOOM)

    def test_seven_boom_case_2(self):
        self.assertEqual(sevenBoom([8, 6, 33, 100]), self.NO_SE_ENCUENTRA_EL_NUMERO)

    def test_seven_boom_case_3(self):
        self.assertEqual(sevenBoom([2, 55, 60, 97, 86]), self.BOOM)

    def test_seven_boom_case_4(self):
        self.assertEqual(sevenBoom([2, 55, 60, 98, 107]), self.BOOM)

class TestRepeticiones(TestCase):

    def test_repeticiones_case_1(self):
       self.assertEqual(repeticiones("AAA", 2), "AA")

    def test_repeticiones_case_2(self):
       self.assertEqual(repeticiones("AAAAAFFFFOOOA", 2), "AAFFOOA")

    def test_repeticiones_case_3(self):
       self.assertEqual(repeticiones("111223333344", 1), "1234")

    def test_repeticiones_case_4(self):
       self.assertEqual(repeticiones("AABB", 1), "AB")


class TestOperacionAritmetica(TestCase):
    def test_arithmetic_operation_case_1(self):
        self.assertEqual(operacion_aritmetica("12 + 12"), 24)

    def test_arithmetic_operation_case_2(self):
        self.assertEqual(operacion_aritmetica("12 - 12"), 0)

    def test_arithmetic_operation_case_3(self):
        self.assertEqual(operacion_aritmetica("12 * 12"), 144)

    def test_arithmetic_operation_case_4(self):
        self.assertEqual(operacion_aritmetica("12 / 6"), 2)

    def test_arithmetic_operation_case_5(self):
        self.assertEqual(operacion_aritmetica("12 / 0"), "No se puede dividir por 0")

class TestCombinaciones(TestCase):
    def test_arithmetic_operation_case_1(self):
        self.assertEqual(combinaciones(['a', 'b', 'c'], 2), ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"])

if __name__ == "__main__":
    unittest.main()