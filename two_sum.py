# Time: O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 26)

print(result)