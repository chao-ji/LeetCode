"""9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

# Solution 1, revert the number digit by digit
# time: O(log10(n)), space: O(1)
class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    # Be aware that reversed `x` might OVERFLOW!
    
    # Corner cases:
    #
    # 1. negative number 
    # 2. numbers with trailing zeros, e.g. 10 100100,
    # can't be palindromic
    if x < 0 or (x % 10 == 0 and x != 0):
      return False

    # At this point, x > 0 and has no trailing zeros
    
    reverted = 0
    while x > reverted:
      reverted = reverted * 10 + x % 10
      x = x // 10

    # at this point, `x` <= `reverted`
    
    # 1. `x` and `reverted` has the same number of digits
    # 2. `x` has one less digit:
    #    `x` = d1 d2 ... dk
    #    `reverted` = d1 d2 ... dk dk+1
    return x == reverted or x == reverted // 10

# Solution 2, convert number to list of digits
# time: O(log10(n)) space: O(log10(n))
class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
      return False
    digits = []

    while x >= 10:
      d = x % 10
      digits.append(d)
      x = (x - d) // 10

    if x > 0:
      digits.append(x)

    l, h = 0, len(digits) - 1
    while l <= h:
      if digits[l] != digits[h]:
        return False
      l += 1
      h -= 1
    return True

