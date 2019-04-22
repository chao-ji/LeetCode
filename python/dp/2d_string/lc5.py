"""5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""
# Solution 1
# DP, time: O(n^2), space: O(n^2)
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
      return ""
    
    n = len(s)
    
    # 2-D dynamic programming
    #
    # dp[i][j], 0 <= i <= j <= n - 1
    # 
    # indicating if substring `s[i]`, ..., `s[j]` is palindromic
    #
    #
    # `s[i]`, ..., `s[j]` is palindromic
    # 
    #  if and only if
    #
    # `s[i]` == `s[j]` and `s[i + 1]`, ..., `s[j - 1]` is palindromic

    # `l` = length of substring, then `j` = `i + l - 1`
    
    palin = [[False for j in range(n)] for i in range(n)]
    low, high, max_len = 0, 0, 1

    # Base cases:
    # all length-1 substrings are trivially palindromic
    for i in range(n):
      palin[i][i] = True

      
    # Now consider substrings with length >= 2
    
    # `l`: length of the substring
    for l in range(2, n + 1):
      # `i`: starting index of the substring
      for i in range(n - l + 1):
        j = i + l - 1 # `j`: ending index of the substring

        if l == 2:
          palin[i][j] = s[i] == s[j]
        else:
          palin[i][j] = s[i] == s[j] and palin[i + 1][j - 1]
       
        if palin[i][j]:
          if l > max_len:
            low, high, max_len = i, j, l

 
    return s[low:high+1]

# Solution 2
# DP, Longest Common substring between S and reversed S, time: O(n^2), space: O(n^2)
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    # Reverse `s`, and use only modified version of
    # LongestCommonSubstring to find the longest palindrom
    
    # s: .....<-------->................
    #         i        j
    #rs: ................<-------->..... 
    #                    i'       j'
    
    # The `<--->` in `rs` must have starting and ending indices 
    # `i'` and `j'`, where
    #
    # `i` == `n` - `j'` and `j` == `n` - `i'` 
    #
    # Otherwise we may have
    #
    # `s` = "abacdfgdcaba"
    # `rs` = "abacdgfdcaba" 
    #
    # the longest common substring is `abacd`, which is not palindromic
    
    r = ''.join(reversed(s))
    sl, sh, tl, th = self.longestCommonSubstring(s, r)
    return s[sl: sh]
    
  def longestCommonSubstring(self, s, t):
    """Find the longest common substring,
    and return that substring.
    
    Args:
      s: string scalar, non empty
      t: string scalar, non empty
    """
    m = len(s)
    n = len(t)
    
    # `dp[i][j]` stores the length of the longest common suffix of 
    # string `s[:i]` and string `s[:j]`
    #    
    # `i` = 0, 1, ..., m - 1
    # `j` = 0, 1, ..., n - 1
    
    #
    #         0   1   2   3   4   5
    #
    #     0   .   .   .   .   .   .       
    #
    #     1   .   .   +   .   .   .
    #                   
    #     2   .   .   .   *   .   .
    #
    #     3   .   .   .   .   .   .
    #
    #     4   .   .   .   .   .   .
    
    # For example,
    # `dp[2][3]` stores the length of the longest common suffix between 
    # `s[:2]` and `t[:3]`
    # 
    # Only when `s[1]` == `t[2]`, `s[:2]` and `t[:3]` have a non-empty common
    # suffix.
    # And it can be extended when `dp[1][2]` > 0
    
    max_len, sl, sh, tl, th = 0, -1, -1, -1, -1
    dp = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
      if s[i] == t[0]:
        dp[i][0] = 1
        sl, sh, tl, th = i, i + 1, 0, 1

    for j in range(n):
      if s[0] == t[j]:
        dp[0][j] = 1
        sl, sh, tl, th = 0, 1, j, j + 1

    for i in range(1, m):
      for j in range(1, n):
        if s[i] == t[j]:
          dp[i][j] = dp[i - 1][j - 1] + 1
          if (dp[i][j] > max_len and
              # The following conditions are to fix the error for finding
              # Longest Palindromic Substring
              i - dp[i][j] + 1 == n - j - 1 and 
              i + 1 == n - j + dp[i][j] - 1
             ):
            max_len = dp[i][j]
            sl, sh, tl, th = i + 1 - dp[i][j], i + 1, j + 1 - dp[i][j], j + 1
    return sl, sh, tl, th

# Solution 3
# Expand from pivot, time: O(n^2), space: O(1)
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
      return s
    
    # The idea is to start from a minimal palindromic substring
    # i.e., "" or "a", and expand it bidirectionally
    
    #  from ""
    #   * * * * * 
    #        ^
    #
    #  from "a"
    #   * * * a * * 
    #         ^

    # We traverse all the pivot locations, including each of the `n`
    # characters and `n` - 1 empty string between characters.
    low, high = -1, -1
    for i in range(len(s)):
      strlen = max(self.expandFromPivot(s, i, i),
                  
                   self.expandFromPivot(s, i, i + 1))
      if strlen > high - low:
        if strlen % 2 == 0:
          low = i - strlen // 2 + 1
          high = i + 1 + strlen // 2
        else:
          low = i - (strlen - 1) // 2
          high = i + (strlen - 1) // 2 + 1
      
    return s[low:high]
    
  def expandFromPivot(self, s, l, r):
    """Expand palindrome substring from a pivot.
    
    `l` and `r` are valid string indices of string `s`, from which
    to expand the palindrome substring.
    """
    
    # At the start of each iteration `s[l + 1]`, ... `s[r - 1]` is 
    # guaranteed to be palindromic
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    return r - l - 1          
          

