# Maxdigit Addition
"""
You are given a list of integer numbers of various digit size and
your task is to find all the numbers which are having maximum digit size

Example 1:

nums = [234,2,34,5,332,90,100]

answer: 666

Explination:
here the maximum digit size is 3 --> 234, 332, 100 (all have 3 digit which is max)

Now return the answer which is the addition of 234 + 332 + 100 == 666

Example 2:

nums = [1024,2,345,6]

answer: 1024

Explination:
here the maximum digit size is 4 --> 1024 (had 4 digits)

Now return the answer which is 1024
"""

import unittest
import math


def add_maxdigit(nums):
    digit_length = []
    for num in nums:
        number_legth = len(str(num))
        digit_length.append(number_legth)
    maximum_length = max(digit_length)
    sum = 0
    for i in nums:
        if len(str(i)) >= maximum_length:
            sum += i
    return sum
    

# DO NOT TOUCH THE BELOW CODE


class TestAddMaxDigit(unittest.TestCase):

    def test_01(self):
        input_nums = [234, 2, 34, 5, 332, 90, 100]
        output_nums = 666

        self.assertEqual(add_maxdigit(input_nums), output_nums)

    def test_02(self):
        input_nums = [1024, 2, 34, 5, 332, 90, 100]
        output_nums = 1024

        self.assertEqual(add_maxdigit(input_nums), output_nums)

    def test_03(self):
        input_nums = [360, 815, 408, 182, 386, 91, 993, 765, 535,
                      553, 680, 569, 438, 817, 428, 65, 783, 187, 600, 45]
        output_nums = 9499

        self.assertEqual(add_maxdigit(input_nums), output_nums)

    def test_04(self):
        input_nums = [547, 1098, 567, 915, 507, 704, 358, 625, 859, 519, 44, 412, 9, 25, 648, 147, 308, 278, 199, 1307, 1334, 348, 595, 1346,
                      1444, 995, 1183, 1161, 587, 813, 738, 308, 370, 674, 1188, 1417, 991, 188, 649, 505, 344, 164, 1318, 61, 346, 1269, 1288, 1241, 339, 940]
        output_nums = 16594

        self.assertEqual(add_maxdigit(input_nums), output_nums)

    def test_05(self):
        input_nums = [12033, 7951, 12482, 11332, 931, 8564, 13803, 2276, 3797, 2364, 10339, 10534, 4231, 13378, 5292, 7964, 1568, 4271, 7964, 11902, 5063, 12082, 13878, 3037,
                      3042, 12339, 10834, 7342, 7444, 8634, 14822, 2712, 9928, 9688, 13906, 11216, 4864, 10767, 8124, 13700, 6445, 5998, 7267, 10765, 5125, 9156, 1045, 7621, 10769, 12818]
        output_nums = 243699

        self.assertEqual(add_maxdigit(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
