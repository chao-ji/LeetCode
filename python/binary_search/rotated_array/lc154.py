"""154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, h = 0, len(nums) - 1
    
    # The following property applies to LC33, LC81, LC153, LC154
    
    # NOTE: if a sorted array (with duplicates or not) is rotated, and `m` is the 
    # midpoint, either the left subarray nums[l], ..., nums[m], or
    # the right subarray nums[m], ..., nums[h]
    # must be increassing (with no duplicates), or non-decreassing (with duplicates).
    #
    # Note if the array is not rotated, both arrays are increassing (with no duplicates),
    # or non-decreassing (with duplicates).
    
    
    # If `nums[m - 1]` > `nums[m]`, `nums[m]` must be the minimum number.
    
    # Otherwise i.e. nums[m - 1] <= nums[m], `m` must be in either of the two non-decreasing 
    # subarrays, left or right.
    #
    
    # 1.
    # if nums[m] < nums[h], then `m`, ..., `h` must be a non-decreassing sequence, and we
    # have at least one number `nums[m - 1]` <= `nums[m] <= numbers in right subarray.
    # So the right subarray can be ruled out from consideration.
    # set `h` = `m` - 1
    
    #         . .|
    # . . . .    | 
    #            |       . .
    #            |. . .
    # l             m      h
    #             m-1
    
    # 2.
    # if nums[m] > nums[h], then `l`, ..., `m - 1`, `m` must be a non-decreassing sequence
    # i.e. the left subarray, which can be ruled out from consideration. So `l` = `m` + 1

    #         . .|
    # . . . .    | 
    #            |       . .
    #            |. . .
    # l   m                h
    #   m-1    
    
    # 3a.
    # if nums[m] == nums[h] == nums[l]
    #
    #
    # . . . . . . . . . . . . . 
    # l           m           h
    
    # all we know is that we can still find the minimum by excluding `nums[l]` and `nums[h]`
    # -- the subarray nums[l + 1], ..., nums[h - 1] is still a rotated sorted array.
    
    # 3b.
    # if nums[l] != nums[m] == nums[h]
    # 
    # Note either nums[m], ..., nums[h] (right) or nums[l], ..., nums[m] (left) must be a 
    # non-decreassing sequence
     
    # if the right subarray is non-decreasing: 
    #    since nums[m] == nums[h], the right array must contain the same repeated number:
    #
    #    so we can rule out the numbers in nums[m + 1], ..., nums[h] while still bounding
    #    the minimum number in nums[l], ... nums[m]: we just set `h` = `m`
    
    # if the left subarray is non-decreassing:
    #
    #
    #
    #       . . . .         .         
    #     .               
    # . .            
    #                
    # l         m      i    h
    # then `nums[l]` must < `nums[m]`
    #
    # we can't have any number `nums[i]` where `m` < `i` < `h`, such that 
    # `nums[i]` != `nums[m]` = `nums[h]`, i.e. `nums[m]`, ..., `nums[h]` contain the same
    # repeated number.
    #
    # so again we can rule out the numbers in nums[m + 1], ..., nums[h] while still bounding
    # the minimum number in nums[l], ... nums[m]: we just set `h` = `m`
    while l <= h:
      m = (l + h) // 2
      if nums[m - 1] > nums[m]:
        break
      elif nums[m] < nums[h]:
        h = m - 1
      elif nums[m] > nums[h]:
        l = m + 1
      else:
        if nums[m] == nums[l]: # worst case O(n)
          l += 1
          h -= 1
        else:
          h = m
    return nums[m]      
