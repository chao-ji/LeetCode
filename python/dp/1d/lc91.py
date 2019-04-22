"""91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution(object):
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # The idea: straightforward to use DP
    
    # prefix                                            suffix
    # .     .     .     .     .     .     .     .       .     .
    #                                                   i-1   i
    #                                           j-1     j
    #
    # Given string `s`, we look at the length-1 suffix `s[i]` and 
    # length-2 suffix `s[i-1]s[i]`
    
    # `i`: the ending index of the suffix, 
    # `j`: the starting index of the suffix, `j` = i - 1, i
    
    # `dp[i]` = the number of ways to decode string `s[0]`, ... `s[i]`
    
    # When `s[i]` or `s[i-1]s[i]` is valid 
    #     when `j` > 0,
    #       `dp[i]` += `dp[j - 1]`    
    #     when `j` == 0,
    #       `dp[j]` = 1
    
    dp = [0 for _ in range(len(s))]
    
    for i in range(len(s)):
      for j in range(max(i - 1, 0), i + 1):
        if self.isValid(s[j:i +1]):
          if j > 0: # prefix is non-empty
            dp[i] += dp[j - 1]
          else: # `j` == 0, prefix is "", and suffix is valid
            dp[i] = 1
    return dp[-1]    
  
  def isValid(self, s):
    if len(s) == 0:
      return True
    elif len(s) == 1:
      s = int(s)
      return s >= 1 and s <= 9
    elif len(s) == 2:
      s = int(s)
      return s >= 10 and s <= 26
    else:
      return False
