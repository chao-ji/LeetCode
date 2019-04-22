"""15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# Solution
# time: O(n^2)
# sorting takes O(nlogn), nested loop takes O(n^2)

class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # The idea: use the solution to LC 167 Two Sum II - Input array is sorted
    # as a subroutine
    
    # We need to sort the numbers in ascending order
    
    # In each iteration, we fixed one of the three numbers: nums[i]
    
    
    # and find all pairs of numbers in 
    
    # nums[i + 1], nums[i + 2], ..., nums[n - 1],
    
    # that add up to `-nums[i]`
    
    nums = sorted(nums)
    
    result = []
    
    for i in range(len(nums) - 2):
      # In the previous iteration, we have found all the pairs picked from 
      
      # nums[i + 1], nums[i + 2], ..., nums[n - 1]
      
      # that add up to `-nums[i]`
      
      # If `nums[i]` == `nums[i - 1]`, we will have a search space that is 
      # a subset of the search space of previous iteration. So we must skip 
      # to the next iteration.
      
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      j, k = i + 1, len(nums) - 1

      while j < k:
        if nums[j] + nums[k] == -nums[i]:
          result.append([nums[i], nums[j], nums[k]])
          
          # If we have found a pair of numbers with index `j` and `k`
          
          # since `nums[j]` + `nums[k]` = constant
          
          # we need to change BOTH numbers to find a NEW pair:
          
          # `nums[j']` != `nums[j]` and `nums[k']` != `nums[k]`
          # j' and k' are the new indices
          j += 1
          k -= 1
          while j < k and nums[j] == nums[j - 1]:
            j += 1
          while j < k and nums[k] == nums[k + 1]:
            k -= 1
        
        elif nums[j] + nums[k] < -nums[i]:
          j += 1
        else:
          k -= 1      
    return result      
