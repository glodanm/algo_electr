import unittest
from main import Electricians


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.e = Electricians(2, [3, 3, 3], 3)
        self.e2 = Electricians(100, [1, 1, 1, 1], 4)


    def test_get_wire_length(self):
        self.assertEqual(self.e.get_wire_length(), 5.66)
        self.assertEqual(self.e2.get_wire_length(), 300)


if __name__ == '__main__':
    unittest.main()