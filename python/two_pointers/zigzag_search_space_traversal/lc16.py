"""16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # The idea: like LC 15 3Sum, we will use the same approach to traverse the 
    # search space in zigzag fashion
    
    nums = sorted(nums)
    dist, closest = float('inf'), 0
    
    for i in range(len(nums) - 2):
      j = i + 1           # low
      k = len(nums) - 1   # high
      while (j < k):
        # if we found three numbers that sum to `target`, the sum is already
        # closest to `target`.
        if nums[j] + nums[k] == target - nums[i]:
          return target
        
        # otherwise, we just take note of the difference between `target`
        # and the sum, and update the smallest distance.
        
        curr_dist = abs(nums[i] + nums[j] + nums[k] - target)
        if curr_dist < dist:
          dist = curr_dist
          closest = nums[i] + nums[j] + nums[k]
          
        # zigzag-traverse the search space 
        if nums[j] + nums[k] < target - nums[i]:
          j += 1
        else:
          k -=1
        
              
    return closest 
