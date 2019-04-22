"""49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from string import ascii_lowercase

class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # The idea:
    
    # We need to map each string in `strs` to a key, then group
    # strings by the key
    
    # To compute the key, we use the counting method:
    
    # 'eat' ==> [1, 0, 0, 0, 1, ..., 1, ... 0]
    #            a           e       t
  
    # 'tea' ==> [1, 0, 0, 0, 1, ..., 1, ... 0]
    #            a           e       t

    # So 'eat' and 'tea' map to the same key.
  
    # string is converted to its 'one-hot' encoding
    
    anagrams = {}
    for s in strs:
      if self.key(s) not in anagrams:
        anagrams[self.key(s)] = []
      anagrams[self.key(s)].append(s)
      
    return list(anagrams.values())  
      
  def key(self, s):
    return tuple([s.count(c) for c in ascii_lowercase])
    
    
