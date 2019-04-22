"""70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    # The idea: straightforward to use DP, See LC377 Combination Sum IV
    
    #
    # dp[i] = number of ways to climb `i` stairs
    #
    # Base case:
    # dp[0] = 1, dp[1] = 1
    #
    # Recursion:
    # To climb `i` stairs, in your last step, you either climb
    #   1 or 2 stair cases:
    #
    #   dp[i] = dp[i - 1] + dp[i - 2]
    #
    # So `dp[i]` is the `i`th Fibonacci number
    
    if n <= 2:
      return n
    
    a = 1   # 1 way to climb 1 stair case
    b = 2   # 2 ways to climb 2 stair cases
    
    
    #       i - 2,      i - 1,      i
    #       a           b           c
    
    #                   i - 1,      i,      i + 1
    #                   a=b         b=c     c=?
    # At the start of each iteration, `a` and `b` are always the two numbers 
    # preceding `c` in the Fibonacci sequence.
    for c in range(3, n + 1):
      c = a + b
      a = b
      b = c
    return c 
        
