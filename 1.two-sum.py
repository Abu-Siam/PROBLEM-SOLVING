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


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i , num in enumerate(nums):
            required = target -num
            if required in seen.keys():
                return [seen[required], i]
            seen[num] = i

print(Solution2().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]


class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = sorted([num,i] for i,num in enumerate(nums))
        left =0
        right = len(nums) - 1
        while left < right :
            current_sum = pairs[left][0] + pairs[right][0]
            if current_sum == target:
                return [pairs[left][1], pairs[right][1]]
            elif current_sum < target:
                left = left + 1               
            elif current_sum > target:
                right = right - 1
               
print(Solution3().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
