"""50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""
class Solution(object):
  def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    # `n` is integer
    
    # Use divide and conquer: each time cut `n` in half
    # until it reaches 0, and the power is 1.
    if n < 0:
      return 1 / self.pow(x, -n)
    else:
      return self.pow(x, n)
      
  def pow(self, x, n):
    # n >= 0
    
    if n == 0:
      return 1.
    
    half = self.pow(x, n // 2)
    if n % 2 == 0:
      # prod = x x x  x x x 
      return half * half
    else:
      # prod = x x x  x x x  x 
      return half * half * x
