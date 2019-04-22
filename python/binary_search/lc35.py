"""35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0 
"""
class Solution(object):
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low, high = 0, len(nums) - 1
    while low <= high:
      mid = (low + high) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        low = mid + 1
      else:
        high = mid - 1
        
    # In binary search, the search space is cut in half in each iteration
    #   * . . . . . . . . . . . . *     
    #     l                     h
    # 
    # At any time we maintain l <= m <= h, where m = (l + h) // 2,
    # '*' on the left denotes -inf
    # '*' on the right denotes inf

    # The LOOP INVARIANT: 
    #   At the start of each iteration
    #     any number to the left of `l` < target
    #     any number to the right of `h` > target
    
    # Eventually, we have eliminated all but one element in the array: 
    #            
    #   * x x x x . x x x x x x x * 
    #             l
    #             h
    #             m
    #
    
    
    # Unless `nums[m]` is the target, we have target > `nums[m]` or target < `nums[m]`
    #
    # In case `target` > nums[m],
    #   the insertion index for `target` would be `l` = `m` + 1, because all the '*' and 'x'
    #   to the left of `l` < target, and all the '*' and 'x' to the right of `m` > target
    
    #               m+1
    #               
    #   * x x x x .   x x x x x x x *               `.` < target
    #               l
    #             h    
    #             m
    
    # In case `target` < nums[m], 
    #   the insertion index for `target` would be `l`, because all the '*' and 'x'
    #   to the left of `l` < target, and all the '*' and 'x' to the right of `h` > target
    #                  
    #   * x x x x   . x x x x x x x *                `.` > target
    #             l
    #           h
    #             m
    
    # Either way the insertion index will always be `l`
    
    return low
    
