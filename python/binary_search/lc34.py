"""34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):
  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    low = self.directedBinarySearch(nums, target, "lower")
    high = self.directedBinarySearch(nums, target, "higher")
    return low, high
    
  def directedBinarySearch(self, nums, target, direction="lower"):
    """Binary search with direction. 
    
    In "lower" direction, we want to search for the left boundary
    In "higher" direction, we want to search for the right boundary
    """
    # left boundary: 
    # nums[l] == target and nums[l - 1] != target
    #
    # . . . . . x x x x x x . . . . .
    #                
    #           ^         
    #           l-bound   
    #
    # or nums[l] == target and l == 0
    # x x x x x x . . . . . . . . . . 
    # ^
    # l-bound
    #
    
    # right boundary:
    
    # nums[r] == target and nums[r + 1] != target
    # . . . . . x x x x x x . . . . .
    #                     ^
    #                     r-bound
    #
    # or nums[r] == target and r == len(nums) - 1
    #
    # . . . . . . . . . . x x x x x x 
    #                               ^
    #                               r-bound
    low, high = 0, len(nums) - 1
    while low <= high:
      mid = (low + high) // 2
      if nums[mid] == target:
        if direction == "lower": 
          # Here we have found the left boundary by definition, return
          if mid == 0 or nums[mid - 1] < target:
            return mid
          
          # otherwise we have
          #
          # . . . . . x x x x x x x
          #             m
          # the left boundary can't be at index >= `mid`
          # so we move `high` down to `mid` - 1
          high = mid - 1
        elif direction == "higher":
          # Here we have found the right boundary by definition, return
          if mid == len(nums) - 1 or nums[mid + 1] > target:
            return mid
          # othewise we have
          #
          # x x x x x x x . . . . . 
          #           m
          # the right boundary can't be at index <= `mid`
          # so we move `low` up to `mid` + 1
          
          low = mid + 1
      elif nums[mid] < target:
        low = mid + 1
      else:
        high = mid - 1
    
    # If `target` did appear in `nums`, the left and right boundary should have been
    # returned at this point
    #
    # So return -1 
    return -1
  

        
