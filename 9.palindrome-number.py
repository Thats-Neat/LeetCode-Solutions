#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        output = ''
        for i in reversed(range(0, len(str(x)))):
            output += str(x)[i]

        return output == str(x)

        
# @lc code=end

