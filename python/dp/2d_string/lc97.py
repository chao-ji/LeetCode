"""97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
class Solution(object):
  def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    l1 = len(s1)    
    l2 = len(s2)
    l3 = len(s3)
    
    if l1 + l2 != l3:
      return False
    
    # `dp[i][j]` = True, if `s1[:i]` and `s2[:j]` can be interleaved to 
    # get `s3[:i + j]`
    # 
    # Here it will be useful to consider the base cases in which one of 
    # the strings is EMPTY:
    #
    # Because interleaving an empty string with a non-empty string has
    #
    # only one outcome.
    
    #         0   1   2   3   4   5   s2
    #
    #     0   T   .   .   .   .   .       
    #
    #     1   .   .   .   .   .   .
    #                   
    #     2   .   .   .   .   .   .
    #
    #     3   .   .   .   .   .   .
    #
    #     4   .   .   .   .   .   .
    #    s1
    
    dp = [[False for j in range(l2 + 1)] for i in range(l1 + 1)]
    
    
    
    # Base cases:
    
    dp[0][0] = True # interleaving "" with "" ==> ""
    
    # `s1` == ""
    # `s2` is non-empty
    # To interleave `s1` and `s2` into `s3`, `s2` and `s3` must have the
    # same prefix
    for j in range(1, l2 + 1):
      # as long as `s2` and `s3` have the same prefix up until now
      if s2[j - 1] == s3[j - 1]:
        dp[0][j] = True
      else:
        break
    
    # `s2` == ""
    # `s1` is non-empty
    # To interleave `s1` and `s2` into `s3`, `s1` and `s3` must have the
    # same prefix
    for i in range(1, l1 + 1):
      # as long as `s1` and `s3` have the same prefix up until now
      if s1[i - 1] == s3[i - 1]:
        dp[i][0] = True
      else:
        break
        
    for i in range(1, l1 + 1):
      for j in range(1, l2 + 1):
        # `s3[i + j - 1]` must be contributed by either 
        # the last char of `s1[:i]` or the last char of `s2[:j]` 
        # 
        # And the prefixes must be interleavable too
        #
        # We need to consider the two possibilities independently
        if s3[i + j - 1] == s1[i - 1]:
          dp[i][j] = dp[i][j] or dp[i - 1][j]
        if s3[i + j - 1] == s2[j - 1]:  
          dp[i][j] = dp[i][j] or dp[i][j - 1]
          
    return dp[l1][l2]      
