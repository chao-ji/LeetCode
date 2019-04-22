"""131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
# See LC 140 Word Break II

# Solution 1, DP
# time: O(n^3), space: O(n^2)
class Solution(object):
  def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    # The idea: straightforward to use dynammic programming
    if not s:
      return []
    
    # First we need a lookup table so we can quickly tell if a substring
    # from `s` is palindromic. See LC5 Longest Palindromic Substring.

    # `palin` has shape [n, n], storing bool values `palin[i][j]`
    # indicating if `s[i:j + 1]` is palindromic 
    n = len(s)
    palin = [[False for j in range(n)] for i in range(n)]
    
    for i in range(n):
      palin[i][i] = True
    
    for l in range(2, n + 1):
      for i in range(n - l + 1):
        j = i + l - 1
        if l == 2:
          palin[i][j] = s[i] == s[j]
        else:
          palin[i][j] = s[i] == s[j] and palin[i + 1][j - 1]

          
          
    # Dynamic programming:      
          
    # dp[i]: the list of different sequences of palindromic strings that
    # string `s[0]`, ..., `s[i]` (`s[:i + 1]`) can be broken into. 
    # If not breakable, dp[i] = []

    # We search for a palindromic suffix `palindrome`, `s[j]`, ..., `s[i]`, 
    # of string `s[:i + 1]`, 

    # .   .   .   .   .   .   .   .   .   .   .   .   .
    #                                                 i
    #                                     j
    #                                     <---suffix-->
    #                                 j-1

    # Then as long as `dp[j - 1]` is not empty, we extend the sequence of palindromic 
    # strings `dp[j - 1]` with the new palindrome s[j:i + 1]
 
  
    dp = []      
    for i in range(n):
      partitions = []
      # Search for suffix `s[j:i + 1]` that is palindromic
      for j in range(i + 1):
        if palin[j][i]:
          # base case
          if j == 0:
            partitions.append([s[j:i + 1]])
          # extend existing sequence of palindromic strings  
          elif dp[j - 1]:
            for sent in dp[j - 1]:
              partitions.append(sent + [s[j:i + 1]])
              
      dp.append(partitions)
      
    return dp[n - 1]    
            
              

# Solution 2, backtracking
class Solution(object):
  def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    if not s:
      return []
    
    n = len(s)
    palin = [[False for j in range(n)] for i in range(n)]
    
    for i in range(n):
      palin[i][i] = True
    
    for l in range(2, n + 1):
      for i in range(n - l + 1):
        j = i + l - 1
        if l == 2:
          palin[i][j] = s[i] == s[j]
        else:
          palin[i][j] = s[i] == s[j] and palin[i + 1][j - 1]
    # The idea: use backtracking
    solutions = []
    self.search([], solutions, 0, s, palin)
    return solutions
    
  def search(self, solution, solutions, start, s, palin):
    if start < len(s):
            
      # Given a partial solution `solution`, which holds a sequence of palindromes
      # of broken from string `s[:start]`, we attempt to extend the solution by 
      # one more palindrome `s[start:end]`

      for end in range(start + 1, len(s) + 1):
        if palin[start][end - 1]:
          solution.append(s[start : end])
          self.search(solution, solutions, end, s, palin)
          solution.pop()
      # BACKTRACK    
      return     
      
    solutions.append(list(solution))  
      
            
              
