"""140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
# See LC131 Palindrome Partitioning

# Solution 1, DP
# time: O(n^3), space: O(n)
class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    # The idea: straightforward to use dynammic programming
    
    dp = []
    wordDict = set(wordDict)

    # use LC 139 as a subroutine to check if `s` is breakable at all
    if not self.breakable(s, wordDict):
      return []
    
    # dp[i]: the list of sentences that string `s[0]`, ..., `s[i]` (`s[:i + 1]`) 
    # can be broken into. If not breakable, dp[i] = []
    
    # We search for a suffix `word`, `s[j]`, ..., `s[i]`, of string `s[:i + 1]`, 
    # which is a word in `wordDict`
    
    # .   .   .   .   .   .   .   .   .   .   .   .   .
    #                                                 i
    #                                     j
    #                                     <---suffix-->
    #                                 j-1
    
    # Then as long as `dp[j - 1]` is not empty, we extend the sentences in
    # `dp[j - 1]` with the new word `word` s[j:i + 1]
    
    for i in range(len(s)):
      sentences = []
      # Search for suffix `s[j:i+1]` that is a word in `wordDict`
      for j in range(i + 1):
        if s[j:i + 1] in wordDict:
          # base case
          if j == 0:
            sentences.append(s[j:i + 1])
          # extend existing sentences
          elif dp[j - 1]:
            for sent in dp[j - 1]:
              sentences.append(sent + ' ' + s[j:i + 1])
      dp.append(sentences)
              
    return dp[len(s) - 1]  
  
  def breakable(self, s, wordDict):
    # Exactly the same as LC 139, test if sequence is breakable into sentences
    n = len(s)
    dp = [False for _ in range(n)]
    
    for i in range(n):
      for j in range(i + 1):
        if (s[j:i + 1] in wordDict
            and (j == 0 or dp[j - 1])):
          dp[i] = True
          break
          
    return dp[-1]


# Solution 2, backtracking
class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    wordDict = set(wordDict)
    # use LC 139 as a subroutine to check if `s` is breakable at all
    if not self.breakable(s, wordDict):
      return []
    
    
    
    # The idea: use backtracking
    solutions = []
    self.search([], solutions, 0, s, wordDict)
    return solutions
      
  def search(self, solution, solutions, start, s, wordDict):
    if start < len(s):
      
      # Given a partial solution `solution`, which holds word list of a sentence
      # broken from string `s[:start]`, we attempt to extend the solution by 
      # one more word `s[start:end]`
      
      for end in range(start + 1, len(s) + 1):
        if s[start:end] in wordDict:
          solution.append(s[start : end])
          self.search(solution, solutions, end, s, wordDict)
          solution.pop()
      # BACKTRACK    
      return 
    solutions.append(' '.join(solution)) 
    
    
  def breakable(self, s, wordDict):
    # Exactly the same as LC 139, test if sequence is breakable into sentences
    n = len(s)
    dp = [False for _ in range(n)]
    
    for i in range(n):
      for j in range(i + 1):
        if (s[j:i + 1] in wordDict
            and (j == 0 or dp[j - 1])):
          dp[i] = True
          break
          
    return dp[-1]    
    
