import unittest

class TestAdditionMethods(unittest.TestCase):

    def test_1(self):
        summ = additionTest(3,4)
        summ.assertEqual(7)

    def test_2(self):
        summ = additionTest(-5,6)
        summ.assertEqual(1)