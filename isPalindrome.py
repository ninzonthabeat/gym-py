import unittest


class Solution:
    # approach 1: reversing the entire number
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        temp = x        # temporary store the initial value

        while temp != 0:
            digit = temp % 10   # extract last digit
            reversed_num = reversed_num * 10 + digit   # add digit
            temp //= 10   # remove last digit and move on to next iteration
        return reversed_num == x
    
    # approach 2: reversing half the number
    def isPalindrome2(self, x: int) -> bool:
        if (x < 0 or (x != 0 and x % 10 == 0)):
            return False   
        reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10   #
            x //= 10    # remove last digit         
        return x == reversed_num or x == reversed_num // 10


# unit tests hooray
class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution
    
    def testIsPalindrome1(self):
        self.assertTrue(solution.isPalindrome1(121))
        self.assertTrue(solution.isPalindrome1(1001))


solution = Solution()
result1 = solution.isPalindrome1(10)
result2 = solution.isPalindrome2(10)
print(result1)
print(result2)

if __name__ == '__main__':
    unittest.main()
