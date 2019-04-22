"""76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
from collections import Counter

class Solution(object):
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not s or not t:
      return ''
    
    # A valid window is defined as one that satisify a certain requirement
    # (i.e. contains all chars in `t`)
    
    # In this algorithm, we keep two pointers `i` and `j`, both initialized to 0,
    # i.e. beginning of the longer string `s`
    
    # We keep doing two things:
    #
    # 1. While the current window `s[j]`, ..., `s[i]` is INVALID, we keep moving
    # `i`, untill `s[j]`, ..., `s[i]` is VALID
    #
    # 2. While the current window `s[j]`, ..., `s[i]` is VALID, we keep moving
    # `j`, untill `s[j]`, ..., `[i]` is INVALID. In the mean time, while the window
    # is VALID, update the length of the valid window.
     

    # Example
    
    # initial state
    # A B A A C B A B
    # i
    # j
    
    # move `i` until the window `s[j]`, ..., `s[i]` is valid 
    # A B A A C B A B
    # j
    #         i
    
    # move `j` until `s[j]`, ..., `s[i]` is invalid while `s[j - 1]`, `s[j]`, ..., `s[i]`
    # is valid
    # A B A A C B A B
    #     j
    #         i
    
    # keep moving `i` until the window `s[j]`, ..., `s[i]` is valid again
    # A B A A C B A B
    #     j
    #           i
    
    
    # The above sliding window algorithm works for ANY "find smallest window" problem
    
    # For this this particular problem, we maintain two variables to keep track of 
    # the validity of the current window
    
    # `w_counter`: maps chars to their counts in the window
    # `filled_counts`: the number of unique chars whose counts meet the requirement
    #
    # Whenever the current window is expanded or contracted, we update these variables.
    
    t_counter = Counter(t)
    w_counter = {}
    
    l, r = 0, 0
    filled_counts = 0
    
    min_len, min_left, min_right = float('inf'), None, None
    
    while r < len(s):
      # Update `w_counter` and `filled_counts` as we add a new char `s[r]` into
      # the current window
      w_counter[s[r]] = w_counter.get(s[r], 0) + 1
      if s[r] in t_counter and w_counter[s[r]] == t_counter[s[r]]:
        filled_counts += 1
      
      while l <= r and filled_counts == len(t_counter):
        # Update the min window length `min_len`, while window is valid.
        if r - l + 1 < min_len:
          min_len, min_left, min_right = r - l + 1, l, r
        
        # Update `w_counter` and `filled_counts` as we delete a char `s[l]` from
        # the current window
        w_counter[s[l]] -= 1
        if s[l] in t_counter and w_counter[s[l]] < t_counter[s[l]]:
          filled_counts -= 1
        
        # While the current window `s[l]`, ..., `s[r]` is valid, contract the window
        l += 1
    
      # While current window `s[l]`, ..., `s[r]` is invalid, expand the window
      r += 1
    
    return s[min_left:min_right + 1] if min_len != float('inf') else ''
      
        
