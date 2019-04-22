"""81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""
class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    low, high = 0,  len(nums) - 1
    # Use binary search where `mid` = (low + high) // 2
    
    # Unless `target` is found, we check 
    # if the right subarray nums[mid], ..., nums[high], or
    #   the left subarray nums[low], ..., nums[mid] is non-decreassing
    
    # if right subarray is non-decreassing, i.e. `nums[mid]` < `nums[high]`
    #        .|
    #    . .  |
    #  .      |
    #         |    . .
    #         |. .
    #  l         m   h
    #  We test if `nums[m]` < `target` <= `nums[h]`:
    #   if so, set `l` = `m` + 1
    #   otherwise, set `h` = `m` - 1     
    
    # if left subarray is non-decreassing, i.e. `nums[mid]` > `nums[high]`
    #        .|
    #    . .  |
    #  .      |
    #         |    . .
    #         |. .
    #  l   m         h
    # We test if `nums[l]` <= `target` < `nums[m]`:
    #   if so, set `h` = `m` - 1
    #   otherwise, set `l` = `m` + 1
    
    # if `nums[mid]` == `nums[high]`, then all we know is that `nums[high]` can't
    # be `target`, because at this point, we have `nums[mid]` !=`target` -- we have
    # not found `target`.
    while low <= high:
      mid = (low + high) // 2
      
      if nums[mid] == target:
        return True
      
      if nums[mid] < nums[high]:
        if nums[mid] < target <= nums[high]:
          low = mid + 1
        else:
          high = mid - 1
      elif nums[mid] > nums[high]:
        if nums[low] <= target < nums[mid]:
          high = mid - 1
        else:
          low = mid + 1
      else: # target != nums[mid] == nums[high]    
            # all we know is  that `nums[high]` can't be `target`
            # so remove it from search space
        high -= 1
    return False    
