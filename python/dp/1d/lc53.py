"""53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
# Solution 1
# DP, O(n)
class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    
    # maxsum_prev
    maxsum_prev = maxsum = nums[0]
  
    for i in range(1, len(nums)):
      # `maxsum_prev` maintains the largest possible sum of subarray ending at `i - 1`
      maxsum_prev = maxsum_prev + nums[i] if maxsum_prev > 0 else nums[i]
      maxsum = max(maxsum, maxsum_prev)
      
    return maxsum 

# Solution 2
# Divide & conquer, O(n)
class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum, _, _, _ = self.maxSum(nums, 0, len(nums) - 1)    
    return max_sum
    
  def maxSum(self, nums, low, high):
    """Compute the sum of maximum subarray in the range [low, high]
    
    Returns:
      sum of maximum subarray
      sum of maximum-sum prefix
      sum of array
      sum of maximum-sum suffix
    """
    if low == high:
      return nums[low], nums[low], nums[low], nums[low]
    
    mid = (low + high) // 2
    
    # array is divided into left and right half at midpoint
    # ....................
    #          m          
    
    
    # 1. Left half:
    #
    # ...****.. 
    #    left: sum of maximum-sum subarray in the left half
    #
    # ****.....
    # max_pref_left: sum of maximum-sum prefix subarray in the left half
    #
    # ......***
    # max_suff_left: sum of maximum-sum suffix subarray in the left half
    #
    # *********
    # left_sum: sum of left half
    
    
    # 2. Right half:
    #
    # ...****..
    #    right: sum of maximum-sum subarray in the right half
    #
    # ****.....
    # max_pref_right: sum of maximum-sum prefix subarray in the right half
    #
    # ......***
    # max_suff_right: sum of maximum-sum suffix subarray in the right half
    #
    # *********
    # right_sum: sum of right half
    
    
    # The max-sum subarray is the max of three cases:
    #                                                           m
    #                                                           |
    # ...***....     or   .....***....      or            ...******..
    #    left                  right              max_suff_left + max_pref_right
    
    # in the mean time, we need to update `max_pref_left` and `max_suff_right`
    #
    # 1.`max_pref_left` is the max of `max_pref_left` and `max_pref_right` + `left_sum`
    #  
    #       m                                    m
    #       |                                    |
    # ****........               or        ***********..
    # max_pref_left                     left_sum + max_pref_right
    #
    # 2. `max_suff_right` is the max of `max_suff_right` and `max_suff_left` + `right_sum`
    #  
    #        m                                               m
    #        |                                               |
    #  ..........****                    or          ....********** 
    #            max_suff_right                max_suff_left + right_sum    
    (left, 
     max_pref_left, 
     left_sum,
     max_suff_left) = self.maxSum(nums, low, mid)
    
    (right, 
     max_pref_right, 
     right_sum,
     max_suff_right) = self.maxSum(nums, mid + 1, high)
          
    max_sum = max(max_suff_left + max_pref_right, max(left, right))
    
    max_pref_left = max(max_pref_left, left_sum + max_pref_right)
    max_suff_right = max(max_suff_right, right_sum + max_suff_left)
    return max_sum, max_pref_left, left_sum + right_sum, max_suff_right 
