"""139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # The idea:
    # enumerate all the suffixes of `s`, and check if
    # 1. The suffix has the desired property (i.e. be a word in `wordDict`)
    # 2. The complementary prefix is empty or breakable
    
    #   prefix                                          suffix
    #   .   .   .   .   .   .   .   .   .   .   .       .   .   .   .   .
    #   0                                       j-1     j               i
    #   
    #   j = 0           , the suffix is the entire string `s`, so the prefix is ""
    #       up to
    #       i       , the suffix has length 1 (it must be non-empty) 
    #      
    # so define `dp[i]` = True, if `s[:i]` is breakable, 0 <= i <= n - 1
    n = len(s)
    dp = [False for _ in range(n)]
    
    for i in range(n): # `i` ending index of suffix, range = 0, ..., n - 1
      for j in range(i + 1): # `j` starting index of suffix, range = 0, ..., i
        if (s[j:i + 1] in wordDict      # whether suffix is in `wordDict`
            and (j == 0 or dp[j - 1])): # whether prefix is empty or breakable
          dp[i] = True
          break
          
    return dp[-1]
