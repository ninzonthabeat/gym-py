from typing import List
import unittest


class Solution:
    def containsDuplicates(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testContainsDuplicates(self):
        self.assertTrue(self.solution.containsDuplicates([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicates([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
