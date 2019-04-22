"""67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # We use 2 pointers `i` and `j`, initially pointing to the least significant 
    # digit of `a` and `b`
    # 
    # `digits` is a list storing the digits of the sum.
    #
    # `bit_sum` is the running variable, storing the digit value of the sum (may
    #   have carryover from previous digit sums). Initialized to 0.
    
    #             . . 
    #               i
    #             . .
    #               j
    #
    #     `bit_sum` = `a[i]` + `b[j]` + `bit_sum`
    #     digits.append(bit_sum % 2)
    #     bit_sum = bit_sum // 2
    #
    #             . . 
    #             i
    #             . .
    #             j
    
    digits, i, j, bit_sum = [], len(a) - 1, len(b) - 1, 0
    while i >= 0 or j >= 0:
      # The iteration continues as long as we have at least one remaining digit
      # to be added, i.e. `i` >= 0 or `j` >= 0
      if i >= 0:
        bit_sum += int(a[i])
        i -= 1
      if j >= 0:
        bit_sum += int(b[j])
        j -= 1
      # current digit value  
      digits.append(str(bit_sum % 2))
      # carry over to the next digit
      bit_sum /= 2
    
    # Don't forget the leading non-zero digit value
    if bit_sum > 0:
      digits.append(str(bit_sum))
    digits = ''.join(digits[::-1])
    return digits
