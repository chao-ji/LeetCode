"""14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
# Solution 1
class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """  
    # The idea: use divide and conquer
    
    # Base case:
    # The LCP of a single string is itself
    
    # If there are > 2 strings, we can recursively divide them into two halves,
    # until we hit the base case. 
    
    #                           s1, s2, s3, s4, s5
    #                           /                 \
    #                        s1, s2            s3, s4, s5
    #                       /   \                /     \
    #                     s1    s2              s3   s4, s5        
    #                                                /    \
    #                                               s4     s5      
    
    # Then we can merge the LCP of smaller problem back to the original problem
    
    #                        LCP(s1, s2, s3, s4, s5)
    #                           /                 \
    #                    LCP(s1, s2)         LCP(s3, s4, s5)
    #                       /   \                /     \
    #                     s1    s2              s3   LCP(s4, s5)        
    #                                                /    \
    #                                               s4     s5          
    
    if len(strs) == 0:
      return ''
    if len(strs) == 1:
      return strs[0]
  
    # Given strings
    # s1, s2, ... smid, smid+1, ..., sn-1    
  
    # We recursively find the LCP of the first half and second half: `left` and `right`
    
    mid = len(strs) // 2
    left = self.longestCommonPrefix(strs[:mid])
    right = self.longestCommonPrefix(strs[mid:])
    
    # The LCP of s1, s2, ... smid, smid+1, ..., sn-1 
    # is simply the LCP of
    # LCP(s1, s2, ... smid) amd LCP(smid+1, ..., sn-1 )
    
    i = 0
    while i < len(left) and i < len(right) and left[i] == right[i]:
      i += 1
      
    return left[:i]   

# Solution 2
# time: O(n*l), n: number of string, l: length of longest string

class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
      return ''
    
    # The idea:
    
    # We grow the LCP one character at a time
    
    # s1: flower
    # s2: flow
    # s3: flight
    
    #
    # s1:     f     l     o     w     e     r   
    # s2:     f     l     o     w
    # s3:     f     l     i     g     h     t
    #         l=0   l=1   ^
    #
    # ^: found mismatch
    
    # Initially the length of LCP is `l` == 0
    
    # In each iteration, we scan the `l`-th character of all strings in `strs`
    
    # If any string does not have the `l`-th charater, or we found a different `l`-th charater, the LCP can't be grown any more, we just return the LCP of length `l`
     
    l = 0
    while True:
      for i in range(len(strs)):
        if not (l < len(strs[i]) and strs[i][l] == strs[0][l]):
          return strs[0][:l]  
      l += 1
      
    # We'll always return from inside the for loop
