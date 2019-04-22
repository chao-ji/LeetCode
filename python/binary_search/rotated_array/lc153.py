"""153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, h = 0, len(nums) - 1
    
    # because all numbers are distinct, the only number whose left neighbor > itself
    # must be the minimum, if this sorted array is rotated at all. 
    #        .|
    #      .  |
    #    .    |
    #  .      |   
    #         |        .
    #         |      .
    #         |    .
    #         |  .
    #         |.
    #          m
    
    # Otherwise i.e. nums[m - 1] < nums[m], `m` must be in either of the two increasing 
    # subarrays, left or right.
    #
    # Note this is true even if the array is not rotated at all.
    
    # if nums[m] < nums[h], then `m - 1`, `m`, ..., `h` must be an increassing sequence
    # i.e. the right subarray, which can be ruled out from consideration. So `h` = `m` - 1
    #        .|
    #      .  |
    #    .    |
    #  .      |   
    #         |        .
    #         |      .
    #         |    .
    #         |  .
    #         |.
    #  l           m   h     
    #            m-1
    
    # if nums[m] > nums[h], then `l`, ..., `m - 1`, `m` must be an increassing sequence
    # which can be ruled out from consideration. So `l` = `m` + 1
    #        .|
    #      .  |
    #    .    |
    #  .      |   
    #         |        .
    #         |      .
    #         |    .
    #         |  .
    #         |.
    #  l   m           h     
    #    m-1    
    
    
    
    
    # NOTE: we compare `num[m]` with `nums[h]` rather than `nums[l]`, because 
    # when nums[l] < nums[m], there are two scenarios :
    
    # 1
    #        .|
    #      .  |
    #    .    |
    #  .      |   
    #         |        .
    #         |      .
    #         |    .
    #         |  .
    #         |.
    #  l   m           h     
    #    m-1    
    #
    # in this case, the minimum is at the right side of `nums[m]`
    
    # 2
    #
    #                 .
    #               . 
    #             .   
    #           .     
    #         .       
    #       .         
    #     .           
    #   .             
    # .               
    # l       m       h
    #
    # in this case, the minimum is at the left side of `nums[m]`
    while l <= h:
      m = (l + h) // 2
      # Found !
      if nums[m - 1] > nums[m]:
        break
      # otherwise, it means  
      # nums[m - 1] < nums[m], since all numbers are distinct 
      elif nums[m] < nums[h]:
        h = m - 1
      else: #i.e. nums[m] > nums[h], since all numbers are distinct
        l = m + 1
    return nums[m]    
