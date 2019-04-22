"""58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
class Solution(object):
  def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
      return 0
    
    # `s` is non-empty from here on.
    
    # `h` will point to the first non space char, from the left 
    h = len(s) - 1
    while h >= 0:
      if s[h] != ' ':
        break
      h -= 1
    
    # `l` will point to the first space char, from the left
    l = h
    while l >= 0:
      if s[l] == ' ':
        break
      l -= 1  

    # normally, the layout of the pointers `l` and `h` looks like
    
    #  "_....._"  
    #   l    h
    # `.` means non-
    
    # in case `s` contains all non-space chars
    #  "......"
    #  l     h
    # l = -1
    
    # or `s` contains all space chars
    #  "______"
    #  h
    #  l
    # l = h = -1
    
    return h - l
