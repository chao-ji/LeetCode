"""18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    quadruplets = []
    
    # The idea: like LC 15 3Sum, we will use the same approach to traverse the 
    # search space in zigzag fashion
    
    # We will fix two numbers `nums[i]` and `nums[j]`, and search for `low` and 
    #`high`, such that
    
    # 0 <= i < j < low < high <= n - 1
    # and 
    # nums[low] + nums[high] == target - nums[i] - nums[j]
    
    for i in range(len(nums) - 3):
      # skip `i`, if `nums[i]` == `nums[i - 1]`, to avoid repeating the search
      # space that is a subset of the search space in the previous iteration
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      
      for j in range(i + 1, len(nums) - 2):
        # skip `j`, if `nums[j]` == `nums[j - 1]`, to avoid repeating the search
        # space that is a subset of the search space in the previous iteration
        if j > i + 1 and nums[j] == nums[j - 1]:
          continue
          
        low, high = j + 1, len(nums) - 1
        while low < high:
          if nums[low] + nums[high] == target - nums[i] - nums[j]:
            quadruplets.append((nums[i], nums[j], nums[low], nums[high]))
            low += 1
            high -= 1
            while low < high and nums[low] == nums[low - 1]:
              low += 1
            while low < high and nums[high] == nums[high + 1]:
              high -= 1
            
          elif nums[low] + nums[high] < target - nums[i] - nums[j]:
            low += 1
          else:
            high -= 1
            
    return quadruplets         
