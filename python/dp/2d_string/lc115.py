"""115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""
class Solution(object):
  def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    ls = len(s)
    lt = len(t)
    if ls < lt:
      return 0
    
    # `dp[i][j]` = the number of distinct subsequences of `s[:i]` that equals `t[:j]`
    #
    # where   0 <= i <= ls,  0 <= j <= lt
    #
    # It will be useful to consider the base cases in which one of `s` or `t`
    # is empty string
    dp = [[0 for j in range(lt + 1)] for i in range(ls + 1)]
    
    # When `s` is empty, the number of distinct subsequences of `s` is always empty
    # and when `t` is non-empty, they cannot be equal. So first row is all zero
    
    # When `t` is empty, there is only ONE subsequence of `s` that equals `t` -- just
    # delete all characters from `s`, you will get `t`. So first col is all one.
    for i in range(ls):
      dp[i][0] = 1
      
    # Base cases:   
    #         0   1   2   3   4   t
    #
    #     0   1   0   0   0   0         
    #
    #     1   1   .   .   .   .   
    #                   
    #     2   1   .   .   .   .   
    #
    #     3   1   .   .   .   .   
    #
    #     4   1   .   .   .   .   
    #     
    #     5   1   .   .   .   .
    #
    #     s  
    
    
    # Example:
    # s = "rabbbit", t = "rabbit"
    # 
    # When we compute `dp[i][j]`, we have two options:
    #
    # 1. Ignore the last char of `s`, and check what is the number of distinct
    #   sequences in `s[:-1]` ("rabbbi") that equals `t` ("rabbit"), i.e. 
    #   dp[i - 1][j]
    #
    # 2. If the last char of `s` and `t` are equal, we can add the additional 
    #   number of distinct subsequences from `d[i - 1][j - 1]`
    #
    
    for i in range(1, ls + 1):
      for j in range(1, lt + 1):
        # option1
        dp[i][j] += dp[i - 1][j]  
        # option2
        if s[i - 1] == t[j - 1]:
          dp[i][j] += dp[i - 1][j - 1]
        
    return dp[ls][lt]
