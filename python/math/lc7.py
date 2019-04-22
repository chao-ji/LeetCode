"""7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    # Be aware that reversed `x` might OVERFLOW!

    # Note: trailing zeros will be removed:
    # 23101000 => 10132
    
    INT_MAX =  2 ** 31 - 1  #  2147483647
    INT_MIN = -2 ** 31      # -2147483648
    
    # Assume input `x` is within range [-2147483648, 2147483647]
    
    # Note: when extracting decimal digits, always try to turn the number 
    # into non-negative integer, by handling the corner cases individually 
    if x == INT_MIN:
      return 0
    
    sign = 1 if x >= 0 else -1
    x = abs(x)
    # at this point `x` is within range [0, 2147483647]
    
    # `x` = d1 d2 ... dn-1 dn
    # `r` = 0
    #
    # ==>
    #
    # `x` = d1 d2 ... dn-1
    # `r` = dn
  
    # Check overflow
    #
    # INT_MAX // 10 = 214748364
    
    # if r <= INT_MAX // 10, then 10*r <= 2147483640, in addition, 
    # we want to make sure adding the additional digit, `x % 10`,
    # wouldn't cause overflow:
    
    # `x % 10` <= 2147483647 - r * 10
    
    r = 0    
    while x > 0:
      if r <= INT_MAX // 10 and INT_MAX - r * 10 >= x % 10:
        # make sure the following would not cause overflow
        r = r * 10 + x % 10
        x = x // 10
      else:
        return 0
      
    return r * sign    
      
 
