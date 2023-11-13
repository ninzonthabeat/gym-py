from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')  # converts string inf val to float inf val
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum

    def maxSubArrayClean(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMaxSubArray(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 6)
        self.assertEqual(self.solution.maxSubArrayClean(nums), 6)


if __name__ == "__main__":
    unittest.main()
