"""87. Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true

Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""
# Solution
# DP, time O(n^4), space: O(n^3)
class Solution(object):
  def isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) != len(s2):
      return False
    
    n = len(s1)
    # The idea is really simple:
    #
    # If two `l`-length strings `s1` and `s2` are scramblable
    
    # Then, `s1` and `s2` can be split into two substrings
    #
    # `s1` = `s1l` + `s1r`,         `len(s1l)` = `len(s2l)` = `p`
    # `s2` = `s2l` + `s2r`,         `len(s1r)` = `len(s2r)` = `l` - `p`
    #
    # `s1`    .   .   .       .   .   .   .   .   .   .
    #         `s1l`           `s1r`
    #         i       i+p-1   i+p                     i+l-1
    #
    # `s2`    .   .   .       .   .   .   .   .   .   .
    #         `s2l`           `s2r`
    #         j       j+p-1   j+p                     j+l-1
    #
    # where 
    #       `s1l` and `s2l` are scramblable,    subproblem #1
    # and   `s1r` and `s2r` are scramblable     subproblem #2
    
    # or
    #   
    # `s1` = `s1l` + `s1r`,         `len(s1l)` = `len(s2r)` = `p`
    # `s2` = `s2l` + `s2r`,         `len(s1r)` = `len(s2l)` = `l` - `p`
    #
    # `s1
    #         .   .   .       .   .   .   .   .   .   .
    #         `s1l`           `s1r`
    #         i       i+p-1   i+p                     i+l-1
    #           
    # `s2`    .   .   .   .   .   .   .       .   .   .
    #         `s2l`                           `s2r`
    #         j                       j+l-p-1 j+l-p   j+l-1
    #
    # where
    #       `s1l` and `s2r` are scramblable,  subproblem #3
    # and   `s1r` and `s2l` are scramblable   subproblem #4
    
    # So the original problem is broken into 4 subproblems, and
    # each subproblem is characterized by 
    # `i` -- the starting index of `s1`, 
    # `j` -- the starting index of `s2`, 
    # `p` -- the length of `s1l` / `s2l`, or `s1l` / `s2r`
    
    
    # Define
    #
    # `dp[l][i][j]` = True, 
    # if `s1[i:i + l]` and `s2[j:j + l]` are scrambable
    # 
    # `i`: starting index in `s1`
    # `j`: starting index in `s2`
    # `l`: length of substring starting at `i` in `s1`, 
    #                      and starting at `j` in `s2`
    
    # s1:       . .   . . . . .   . . . 
    #                 i
    # s2:       .   . . . . .   . . . . 
    #               j
    dp = [[[False for j in range(n)] for i in range(n)] for l in range(n + 1)]
    
    # we compare two substrings 
    for l in range(1, n + 1): # len of substring
      for i in range(n - l + 1):
        for j in range(n - l + 1):
          
          # Base case:
          # if len == 1, simply compare the characters
          if l == 1: # len == 1
            dp[l][i][j] = s1[i] == s2[j]
          else:
            for p in range(1, l + 1):
              if (
                (dp[p][i][j] and 
                 dp[l - p][i + p][j + p]) or 
                (dp[p][i][j + l - p] and 
                 dp[l - p][i + p][j])
              ):
                dp[l][i][j] = True
                break
                
    return dp[n][0][0]            
