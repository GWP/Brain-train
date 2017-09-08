import unittest
from util import is_valid_problem_input, get_digits, generate_numbers

class TestUtil(unittest.TestCase):
    def test_is_valid_problem_input_pos(self):
        pt = 'add'
        diff = '2'
        expected = True
        self.assertEqual(is_valid_problem_input(pt, diff), expected)

    def test_is_valid_problem_input_neg_pt(self):
        pt = 'ad'
        diff = '2'
        expected = False
        self.assertEqual(is_valid_problem_input(pt, diff), expected)

    def test_is_valid_problem_input_neg_diff(self):
        pt = 'add'
        diff = 2
        expected = False
        self.assertEqual(is_valid_problem_input(pt, diff), expected)

    def test_get_digits(self):
        diff = 4
        expected = 3, 2
        self.assertEqual(get_digits(diff), expected)

    def test_get_digits_2(self):
        diff = 3
        expected = 2, 2
        self.assertEqual(get_digits(diff), expected)

    def test_generate_numbers_sub(self):
        pt = 'sub'
        diff = 2
        for _ in range(100):
            actual = generate_numbers(pt, diff)
            self.assertEqual(len(actual), 2)
            self.assertNotEqual(actual[0], 0)
            self.assertNotEqual(actual[1], 0)
            self.assertTrue(actual[0] < 10000)
            self.assertTrue(actual[0] > -10000)

    def test_generate_numbers_div(self):
        pt = 'div'
        diff = 3
        for _ in range(100):
            actual = generate_numbers(pt, diff)
            self.assertEqual(len(actual), 2)
            self.assertNotEqual(actual[0], 0)
            self.assertNotEqual(actual[1], 0)
            self.assertTrue(actual[0] <= 100, "actual was {}".format(actual[0]))
            self.assertTrue(actual[0] >= 0, "actual was {}".format(actual[0]))
            self.assertTrue(actual[1] <= 100, "actual was {}".format(actual[1]))
            self.assertTrue(actual[1] >= 0, "actual was {}".format(actual[1]))

    def test_generate_numbers_neg(self):
        pt = 'hex'
        diff = 2
        with self.assertRaises(AssertionError):
            generate_numbers(pt, diff)

if __name__ == '__main__':
    unittest.main()