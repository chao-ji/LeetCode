"""33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
      return -1
    
    low, high = 0, len(nums) - 1
    
    # Use binary search where `mid` = (low + high) // 2
    
    # Unless `target` is found, we check 
    # if the right subarray nums[mid], ..., nums[high], or
    #   the left subarray nums[low], ..., nums[mid] is increassing
    
    # if right subarray is increassing, i.e. `nums[mid]` < `nums[high]`
    #        .|
    #      .  |
    #    .    |
    #  .      |
    #         |      .
    #         |    .
    #         |  .
    #         |.
    #  l         m   h
    #  We test if `nums[m]` < `target` <= `nums[h]`:
    #   if so, set `l` = `m` + 1
    #   otherwise, set `h` = `m` - 1 
    
    # if left subarray is increassing, i.e. `nums[mid]` > `nums[high]`
    #        .|
    #      .  |
    #    .    |
    #  .      |
    #         |      .
    #         |    .
    #         |  .
    #         |.
    #  l   m         h    
    # We test if `nums[l]` <= `target` < `nums[m]`:
    #   if so, set `h` = `m` - 1
    #   otherwise, set `l` = `m` + 1
    
    # NOTE: if `target` is not in array, `mid` ends up pointing to the INDEX
    # where `target` is to be inserted in either of the two increasing subarrays
    # We check `mid` is in valid range, and if `nums[mid]` == `target`. 
    
    while low <= high:
      mid = (low + high) // 2
      
      if nums[mid] == target:
        break
      
      if nums[mid] < nums[high]:
        if nums[mid] < target <= nums[high]:
          low = mid + 1
        else:
          high = mid - 1
      else: # nums[mid] > nums[high]
        if nums[low] <= target < nums[mid]:
          high = mid - 1
        else:
          low = mid + 1
          
    if 0 <= mid <= len(nums) - 1 and nums[mid] == target:
      return mid
    return -1 
        
