from kdistinctchar import longest__string_k_distinct
import unittest

class TestKD(unittest.TestCase):
    def test_basicArray(self):
        expected = 3
        example = ['a', 'b', 'a', 'g', 'h', 'r', 'y', 'e', 'h', 'j']
        actual = longest__string_k_distinct(example, 2)
        self.assertEqual(expected, actual)

    def test_rejectsWrongArray(self):
        example = [1, 2, 3, 4]
        with self.assertRaises(Exception):
            longest__string_k_distinct(example, 2)

if __name__ == '__main__':
    unittest.main()