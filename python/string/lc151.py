"""151. Reverse Words in a String

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""
class Solution(object):
  def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
      return ''
    
    # First, find the last word, See LC58
    h = len(s) - 1
    while h >= 0:
      if s[h] != ' ':
        break
      h -= 1
    
    l = h
    while l >= 0:
      if s[l] == ' ':
        break
      l -= 1  
    
    # `l` points to the space char preceding the last word
    
    # if `l` > 0
    #   recurse on `s[:l]` to get the reversed words in the prefix
    # otherwise, the prefix is empty
    remaining = self.reverseWords(s[:l]) if l > 0 else ''  
    if not remaining:
      return s[l + 1: h + 1]
    else:
      return s[l + 1: h + 1] + ' ' + remaining
