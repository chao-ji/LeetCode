"""72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""
class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)
    if not m:
      return n
    elif not n:
      return m
    
    # Dynamic programming
    # `dp[i][j]` = the minimum edit distance between `word1[:i]` and `word2[:j]`
    
    # `i` = 0, 1, ..., m
    #
    # `j` = 0, 1, ..., n
    
    #         0   1   2   3   4   5   word2
    #
    #     0   0   1   2   3   4   5       
    #
    #     1   1   .   +   .   .   .
    #                   
    #     2   2   .   .   *   .   .
    #
    #     3   3   .   .   .   .   .
    #
    #     4   4   .   .   .   .   .
    # word1
    
    # First row: edit distance between "" (word1) and word2[:j]
    # First col: edit distance between "" (word2) and word1[:i]
    
    # dp[i-1][j-1]          dp[i-1][j]
    #
    # dp[i][j-1]            dp[i][j]
    
    
    dist = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
      dist[i][0] = i
    for j in range(1, n + 1):
      dist[0][j] = j
    
    for i in range(1, m + 1):
      for j in range(1, n + 1): 
        # substitution:
        
        # We already have the optimal alignment from 
        #
        # word1[0], ..., word1[i - 1]           to
        #
        # word2[0], ..., word2[j - 1]
        # 
        # now we just replace `word1[i]` with `word2[j]`
        diag = dist[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
        # insertion:
        
        # We already have the optimal alignment from
        # 
        # word1[0], ..., word1[i - 1]           to
        #
        # word2[0], ..., word2[j - 1], word2[j]
        # 
        # now we just insert `word1[j]` at the end of `word1[j - 1]`
        up = dist[i - 1][j] + 1
        # deletion
        
        # We already have the optimal alignment from
        #
        # word1[0], ..., word1[i - 1], word2[i] to
        #
        # word2[0], ..., word2[j - 1]  
        #
        # now we just delete `word2[j]` from `word2` 
        left = dist[i][j - 1] + 1
        
        dist[i][j] = min(min(diag, up), left)
    return dist[m][n]    

