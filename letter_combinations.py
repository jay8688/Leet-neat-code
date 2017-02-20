"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


# http://www.cnblogs.com/zuoyuan/p/3779761.html
# 解题思路：穷举所有可能的字符串使用dfs来解决。
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return

            for letter in dict[digits[num]]:
                dfs(num+1, string+letter, res)

        if len(digits) == 0:
            return []

        res = []
        length = len(digits)
        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        dfs(0, '', res)
        return res
