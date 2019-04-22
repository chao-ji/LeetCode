"""3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
      return 0
    
    # The idea:
    # Use two pointers `l` and `r` to keep track of the longest substring
    # without repeating characters
    
    # Initially put both `l` and `r` at the beginning of string
    # and move `r`
    
    #   .   .   .   .   .   .   .
    #   l
    #   r
    
    # As we move `r`, always record the most recent index at which 
    # each unique char occurred
    
    #   .   .   .   .   .   .   .
    #   l                       r
    #           ^ 
    #           last seen    
    
    # When we hit a character that has already been discovered before,
    # and if its most recent index (`^`) >= l, it means we have a repeated 
    # character, we have to restart the substring from the next index
    # i.e. `^` + 1
    
    last_seen = {}
    l, r = 0, 0
    
    max_len = 0
    
    # At the start of each iteration, 
    # 1. `last_seen` always stores the most recent index of all characters 
    #   before index `r`,
    # 2. subtring `s[l]`, ..., `s[r]` has no repeating characters.
    
    while r < len(s):
      if s[r] in last_seen and last_seen[s[r]] >= l:
        max_len = max(max_len, r - l)
        
        l = last_seen[s[r]] + 1
      last_seen[s[r]] = r
      r += 1
    
    max_len = max(max_len, len(s) - l)
    return max_len    
