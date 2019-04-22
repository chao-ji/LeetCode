"""343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

"""
class Solution(object):
  def integerBreak(self, n):
    """
    :type n: int
    :rtype: int
    """
    # The idea: straightforward to use DP 
    # See LC 279, LC 322
    
    # 0       1    ...  i-k  ...      i-3     i-2     i-1     i                 
    # .       .                       .       .       .       .  
    # <-- maybe breakable ------------- >     <- unbreakable ->
    # 
    #                               ...     ...
    #
    # <- maybe breaka-> <----------- unbreakable ------------->
    
    # `dp[i]` = the max product by breaking `i` into positive integers
    # 0 <= i <= n
    # 
    
    # Base case:
    # dp[1] = 1, the number of 1 can't be broken in to >= 2 positive integers
    
    # Given target integer `i`, 
    
    # we can pick the first positive integer 1 <= `j` <= `i` - 1, which results
    # in the second integer `i` - `j`
    # 
    # Note:
    #   1. the first integer `j` is always kept as is in the product (i.e. unbreakable)
    #   2. we can choose whether to keep breaking `i` - `j`, OR
    #       treating it as a single integer (i.e. unbreakable) in the product
    #     i.e. dp[i - j] * j, or (i - j) * j  
    # 
    # i.e., we need to choose which `j` maximize 
    # the MAXIMUM of `dp[i - j] * j` and  `(i - j) * j`
    
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    
    for i in range(2, n + 1):
      for j in range(1, i):
        dp[i] = max(max(dp[i], dp[i - j] * j), (i - j) * j)
        
    return dp[n]    
    
