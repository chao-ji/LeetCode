"""279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution(object):
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    # The idea: straightforward to use DP 
    # See LC 322
    
    # 0       1    ...  i-nk  ...     i-n3    i-n2    i-n1    i                 
    # .       .                       .       .       .       .  
    #                                         <- sq num `n1` ->
    # 
    #                               ...     ...
    #
    #                   <----------- sq num `nk' ------------->

    # `dp[i]` = the least number of squares that add up to `i`
    # 0 <= i <= n
    #       
    
    # `dp[i]` is like the number of "jumps" to get from 0 to `i`, where
    # the "length" of each jump must be a square number.

    # Base case:
    # dp[0] = 0: 0 number is needed to add up to 0
    # dp[1] = 1: one number, i.e. 1, is needed to add up to 1 
    
    # Given target amount `i`, 
    #
    # We need to find which square number `k` <= `i` that results in
    # the minimum numbers that add up to `i`
    # 
    # i.e., which `k` minimizes `dp[dp[i] - k]`
    
    # Instead of checking if `k` is square, we make square numbers
    # 
    # based on the square root `j`: `k` = `j` * `j`
    
    dp = [0 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
      # the maximum possible number of square numbers for `i` is `i`
      # i.e., `i` = `i` * 1
      dp[i] = i
      
      j = 1
      while j * j <= i:
        dp[i] = min(dp[i], 1 + dp[i - j * j])  
        j += 1
        
    return dp[n]
