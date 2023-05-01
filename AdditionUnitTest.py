import unittest

class TestAdditionMethods(unittest.TestCase):

    def test_1(self):
        summ = additionTest(3,4)
        summ.assertEqual(7)
        print("test_1 success")

    def test_2(self):
        summ = additionTest(-5,6)
        summ.assertEqual(1)
        print("test_2 success")
