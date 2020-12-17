# Boss Fight
"""
You are given a list of integers fighters and a two dimensional list bosses. The fighters list contains 1s and 0s with a 1 representing a fighter. Similarly, each bosses list contains 1s and 0s with a 1 representing a boss.

Given that fighters can beat a bosses row if it contains more fighters than bosses, return a new bosses matrix with defeated boss rows removed.

Example 1
Input

fighters = [0, 1, 1]
bosses = [[0, 0, 0],
[0, 0, 1],
[0, 1, 1],
[1, 1, 1]]
Output

[[0, 1, 1],
[1, 1, 1]]
Explanation

There's 2 fighters so is able to beat [0, 0, 0] and [0, 0, 1] bosses.
"""

import unittest


def winning_Bosses(fighters, bosses):
    bosses_dup = bosses
    bosses=[]
    for boss_matrix in bosses_dup:
        if boss_matrix.count(1) >= fighters.count(1):
            bosses.append(boss_matrix)

    return bosses_dup
    


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestWinningBosses(unittest.TestCase):

    def test_01(self):
        fighters = [0, 1, 1]
        bosses = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
        ans = [[0, 1, 1], [1, 1, 1]]
        self.assertEqual(winning_Bosses(fighters, bosses), bosses)

    def test_02(self):
        fighters = [0, 1, 1]
        bosses = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
        ans = [[0, 1, 1], [1, 1, 1]]
        self.assertEqual(winning_Bosses(fighters, bosses), bosses)

    def test_03(self):
        fighters = [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
        bosses = [[0, 0, 0, 0], [0, 0, 1, 1, 1, 1],
                  [0, 1, 1], [1, 1, 1, 1, 1, 1]]
        ans = [[1, 1, 1, 1, 1, 1]]
        self.assertEqual(winning_Bosses(fighters, bosses), bosses)


if __name__ == '__main__':
    unittest.main(verbosity=2)
