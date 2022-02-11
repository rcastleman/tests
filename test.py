import unittest
from my_sum import sum
from fractions import Fraction


# target = __import__("my_sum.py")
# sum = target.sum


class TestSum (unittest.TestCase):

    def test_list_int(self):
        """
        test: sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)

        self.assertEqual(result,6)
    
    def test_list_fracion(self):
        """
        Test that the function can sum fractions"""
        data = [Fraction(1,4),Fraction(1,4),Fraction(2,5)]
        result = sum(data)
        self.assertNotEqual(result,1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()

