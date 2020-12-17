# List of Narcissistic number
"""
Given a range of numbers of base 10 get the list of Narcissistic numbers in the range

Narcissistic numbers are the numbers which gives the answer as the number itself if each digit raised 
to the power of total number of digits in the number are added.

Example 1
Input
n = 154 -> range upto 154

Output

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]

Explanation
0 = 0**1 == 0
to
153 = 1 ** 3 + 5 ** 3 + 3 ** 3 == 153
"""
import unittest


def narcissistic_number(n):
    output = []
    for number in range(n):
        sum = 0
        length = len(str(number))
        for digit in str(number):
            sum = sum + int(digit) ** length
            if sum == number:
                output.append(number)
    output1 = []
    for i in output:
        if i not in output1:
            output1.append(i)
    return output1


class NarcissisticNumber(unittest.TestCase):

    def test_01(self):
        input_num = 154
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_02(self):
        input_num = 323
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_03(self):
        input_num = 371
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_04(self):
        input_num = 1635
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_05(self):
        input_num = 1634
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

        self.assertEqual(narcissistic_number(input_num), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
