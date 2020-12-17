"""
??? Question with two examples ???
"""

import unittest


def decode_from_dict(dictionary):
    string = ""
    length = 0
    for value in dictionary.values():
        length += len(value[0])
    ##Creating temporary list
    temp_list = [0] * length
    ###Created temporary List
    present = 1
    for k in dictionary.keys():
        ##Getting a characte from the key
        letter = chr(k)
        ##Getting values of the key
        dict_value = dictionary[k]
        ##Checking the number of occurance of a character
        if temp_list.count(letter) < dict_value[1]:
            ##GETTING THE INDEX VALUE TO BE PLACED FROM VALUE
            for index in dict_value[0]:
                ##REPLACING THE 0 WITH CHARACTER THAT WE GOT FROM KEY (line 15)
                temp_list[index] = letter
    ##Merging items in "temp_list" into a string
    for character in temp_list:
        string += character
    return (string)
    #write your code here


# DO NOT TOUCH THE BELOW CODE
class TestDecodeFromDict(unittest.TestCase):

    def test_01(self):

        d = {112: [[0, 2], 2], 97: [[1, 3], 2]}
        output = "papa"

        self.assertEqual(decode_from_dict(d), output)

    def test_02(self):

        d = {107: [[0], 1], 114: [[1], 1], 97: [[2], 1], 110: [
            [3], 1], 116: [[4], 1], 104: [[5], 1], 105: [[6], 1]}
        output = "kranthi"

        self.assertEqual(decode_from_dict(d), output)

    def test_03(self):

        d = {84: [[0], 1], 104: [[1, 12], 2], 105: [[2, 9, 15], 3], 115: [[3, 10], 2], 32: [[4, 8, 11, 18], 4], 98: [[5], 1], 111: [
            [6, 20], 2], 120: [[7], 1], 97: [[13], 1], 118: [[14], 1], 110: [[16], 1], 103: [[17, 19], 2], 108: [[21], 1], 100: [[22], 1]}
        output = "This box is having gold"

        self.assertEqual(decode_from_dict(d), output)

    def test_04(self):

        d = {84: [[0], 1], 104: [[1], 1], 105: [[2, 10], 2], 115: [[3], 1], 32: [[4, 8], 2], 100: [
            [5], 1], 111: [[6], 1], 99: [[7], 1], 108: [[9], 1], 110: [[11], 1], 107: [[12], 1]}
        output = "This doc link"

        self.assertEqual(decode_from_dict(d), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
