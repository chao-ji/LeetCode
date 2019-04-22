"""66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # We run through the array from the least significant digit 
    # to the most significant digit
    
    # 3 1 4 1 5 9
    #           ^
    #           1: bit_sum
    
    # => 
    #              Add `bit_sum` to current digit
    # 3 1 4 1 5 10
    #           ^
    # =>           Compute the value left at current digit and the `carry`
    #              Move on to the next digit
    # 3 1 4 1 5 0
    #         ^
    #         1: bit_sum  
    #
    # `bit_sum` maintains the value yet to be added to the current digit
    
    result_digits, i, bit_sum = [], len(digits) - 1, 1
    while i >= 0:      
      # The iteration continues as long as we have one remaining digit, i.e. i >= 0
      bit_sum += digits[i]
      i -= 1
      
      result_digits.append(bit_sum % 10) # current digit value  
      bit_sum /= 10 # carry over to the next digit
    
    # Don't forget the leading non-zero digit value
    if bit_sum > 0:
      result_digits.append(bit_sum)
      
    return result_digits[::-1]    
