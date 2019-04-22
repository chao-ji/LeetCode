"""132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
# Solution, DP
# time: O(n^2), space: O(n^2)
class Solution(object):
  def minCut(self, s):
    """
    :type s: str
    :rtype: int
    """
    # The idea: we need to quickly tell if a substring is palindromic or not
    
    # Step1: 
    # build a lookup table `palin` where
    # `palin[i][j]` = True, if `s[i]`, ..., `s[j]` is palindromic
    
    # `s[i]`, ..., `s[j]` is palindromic
    # 
    #  if and only if
    #
    # `s[i]` == `s[j]` and `s[i + 1]`, ..., `s[j - 1]` is palindromic

    # `l` = length of substring, then `j` = `i + l - 1`
    
    n = len(s)
    palin = [[False for j in range(n)] for i in range(n)]
    
    # Base cases:
    # all length-1 substrings are trivially palindromic
    for i in range(n):
      palin[i][i] = True
      
    # `l`: length of the substring
    for l in range(2, n + 1):
      # `i`: starting index of the substring
      for i in range(n - l + 1):
        j = i + l - 1 # `j`: ending index of the substring

        if l == 2:
          palin[i][j] = s[i] == s[j]
        else:
          palin[i][j] = s[i] == s[j] and palin[i + 1][j - 1]
    
    # Step2: 
    # Use DP to find the minimum number of cuts:
    #
    # enumerate all the suffixes of `s`, and check if
    # 1. The suffix has the desired property (i.e. palindromic)
    # 2. If so, what is the min cuts of the complementary prefix 
    #
    # Find the suffix that results in the minimum cuts
    
    #   prefix                                          suffix
    #   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .
    #   0                                       j-1     j               i
    #   
    #   j = 0           , the suffix is the entire string `s`, so the prefix is ""
    #       up to
    #       i       , the suffix has length 1 (it must be non-empty) 
    
    dp = [0 for i in range(n)]
    
    for i in range(n): # `i` ending index of suffix, range = 0, ..., n - 1

      min_cut = i
      for j in range(i + 1): # `j` starting index of suffix, range = 0, ..., i
        # check if substring `s[j:i + 1]` is palindromic
        if palin[j][i]:
          min_cut = min(min_cut, dp[j - 1] + 1 if j > 0 # At least one cut is needed 
                        else 0  # the entire string s[:i] is palindromic, no cut is needed
                       )
      dp[i] = min_cut
      
    return dp[-1]
