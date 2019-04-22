"""125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
import string

class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
      return True
    
    # The idea:
    #   compare one pair of characters at a time, and then move both pointers
    #   until they both point to alphanumeric chars.
    
    #     .     .     *     .     .     .     .     *     .     .
    #     l ==>                                             <== h                               
    #
    #     move `l` up and `h` down, until they both point to alphanumeric chars
    #
    #     .     .     *     .     .     .     .     *     .     .
    #                 l                             h
    
    #   In each iteration, we
    #     1. increment `l` until it points to an alphanumeric char
    #     2. decrement `h` until it points to an alphanumeric char
    #     3. compare `s[l]` and `s[h]`
    #     4. do `l` += 1 and `h` -= 1
    #
    #   At any point in the loop, we need to make sure that `l` <= `h`.
    
    valid_chars = set(string.ascii_letters + string.digits)
    
    l, h = 0, len(s) - 1
    while l <= h:
      while l <= h and s[l] not in valid_chars:
        l += 1
      while l <= h and s[h] not in valid_chars:
        h -= 1
      
      if l <= h and s[l].lower() != s[h].lower():
        return False
      l += 1
      h -= 1
        
    return True    
