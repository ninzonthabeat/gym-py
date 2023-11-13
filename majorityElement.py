from typing import List
from collections import defaultdict
import unittest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        n = n // 2
        for key, value in m.items():
            if value > n:
                return key

        return n


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMajorityElement(self):
        nums = [3, 2, 3]
        self.assertEqual(self.solution.majorityElement(nums), 3)

        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(self.solution.majorityElement(nums), 2)


if __name__ == "__main__":
    unittest.main()
