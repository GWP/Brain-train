import unittest
from most_frequent_int import mostFreqInt


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def true_test(self):
        print('running test!')
        intArr = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 3, 8, 7]
        self.assertEqual(mostFreqInt(intArr), 7)


if __name__ == '__main__':
    unittest.main()
