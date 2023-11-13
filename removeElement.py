from typing import List
import unittest


class Solution:
    def removeElement(self, nums: List[int],
                      val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testRemoveElement(self):
        nums = [3, 2, 2, 3]
        self.assertEqual(self.solution.removeElement(nums, 3), 2)
        nums = [3, 2, 2, 3]
        self.assertEqual(self.solution.removeElement(nums, 2), 2)


if __name__ == '__main__':
    unittest.main()