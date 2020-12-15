import unittest
from main import KahanSum


class MyTestCase(unittest.TestCase):
    def test1(self):
        arr = [0.987654321, 0.369]
        res = 1.356654321
        self.assertEqual(KahanSum(arr), res)
    def test2(self):
        arr = [13.258, 158.269852, 0.00000001]
        res = 171.52785201
        self.assertEqual(KahanSum(arr), res)


if __name__ == '__main__':
    unittest.main()
