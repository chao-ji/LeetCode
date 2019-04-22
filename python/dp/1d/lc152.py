"""152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution(object):
  def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Use the same strategy as maximum sum subarray -- we keep track of the product of 
    # the max-product subarray, ending exactly at current index `i`, and see if we can
    # increase the product by multiplying the product of some subarray ending at `i - 1`
    
    # BUT here we need to consider the sign of `nums[i]` and the product of subarray
    # ending at `i - 1` (denoted as `prod[i - 1]`)
    
    # If `nums[i]` == 0, we are done -- the max product subarray ending at `i` is
    #   always going to be zero
    
    # If `nums[i]` > 0, we want the `prod[i - 1]` > 1 and is the largest, so
    #   we can increase `nums[i]` by multiplying `nums[i]` with `prod[i - 1]`
    
    # If `nums[i]` < 0, we can still increase the product, if `prod[i - 1]` <= -1
    #   and is the smallest
    
    # So we need to keep track of both the product of max-product subarray and the 
    # the product of min-product subarray ending at each index
    
    max_prod_sofar = [0 for _ in range(len(nums))]
    min_prod_sofar = [0 for _ in range(len(nums))]
    
    max_prod_sofar[0] = nums[0]
    min_prod_sofar[0] = nums[0]
    
    for i in range(1, len(nums)):
      max_prod_sofar[i] = nums[i]
      min_prod_sofar[i] = nums[i]
      
      if nums[i] > 0:
        if max_prod_sofar[i - 1] > 1:
          max_prod_sofar[i] *= max_prod_sofar[i - 1]
          
        if min_prod_sofar[i - 1] <= -1:
          min_prod_sofar[i] *= min_prod_sofar[i - 1]
        
      elif nums[i] < 0:  
        if min_prod_sofar[i - 1] <= -1:        
          max_prod_sofar[i] *= min_prod_sofar[i - 1]
        if max_prod_sofar[i - 1] > 1:
          min_prod_sofar[i] *= max_prod_sofar[i - 1]
          
    return max(max_prod_sofar)    
