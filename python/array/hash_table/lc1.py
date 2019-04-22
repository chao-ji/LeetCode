"""1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # The idea:
    
    # Upon seeing a new number `nums[i]`, we check if its complement `target` - `nums[i]`
    # was previously seen.
    
    # We always save the current number `nums[i]` by storing it is a hashmap
    
    # mapping it to its index `i`
    # map[nums[i]] = i   
    
    complement = {}
    for i in range(len(nums)):
      if target - nums[i] in complement:
        return [complement[target - nums[i]], i]
      complement[nums[i]] = i
