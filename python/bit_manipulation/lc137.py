"""137. Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Normally we don't have to do the following, it's mean  
    # to deal with the input that contains negative numbers
    minval = min(nums)
    if minval < 0:
      for i in range(len(nums)):
        nums[i] -= minval
        
    single = self.singleNumberNonNegative(nums)
    
    # Normally we don't have to do the following, it's mean  
    # to deal with the input that contains negative numbers
    if minval < 0:
      return single + minval
    else:
      return single
    
  def singleNumberNonNegative(self, nums):   
    result = 0
    
    NUM_BITS = 32
    # assume numbers in `nums` are 32-bit signed integers
    # determine the bit value of each of the 32 digits and for all numbers in `nums` 
    # 
    # for example, nums = [2, 2, 3, 2]
    # their bits:
    # 010
    # 010
    # 011
    # 010
    # the count of 1's at the second digit is 4 (% 3 == 1), and at the first digit is 1
    # (% 3 == 1)
    # so the binary representation is 011
    for i in range(NUM_BITS) : 
       
      # `mask` is a binary mask with only one bit "on" at a time:
      #
      #   i       mask
      #
      #   0       0 ... 001
      #   1       0 ... 010
      #   2       0 ... 100
      #   ...     ...
      
      num_ones = 0
      mask = (1 << i) 
      for j in range(len(nums)): 
        if (nums[j] & mask):    # logical AND zeros out all BUT the `i`'s digit 
          num_ones = num_ones + 1

      # If `num_ones` is not multiple of 3 at digit `i`, then the result value
      # have `i`'s digit "on",
      
      # Example:
      # 
      #   i         mask
      #   0         0001
      #   2         0100
      #   3         1000
      
      #   result = 0 + 0001 + 0100 + 1000 = 1101 (13)
      if num_ones % 3 == 1: 
        result = result + mask 
        
    return result  
