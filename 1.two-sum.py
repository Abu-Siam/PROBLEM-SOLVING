#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            required = target - nums[i]
            if required in nums[i + 1:]:
                return [i, nums.index(required)]
# @lc code=end

print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]