"""17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
      return []
    
    # The idea: straightforward to use Recursion
    
    # This is a typical recursion problem. The size of the problem is characterized by
    # the length of the string `digits`.
    
    # The Recurion function always returns a list of strings.
    
    # Base case:
    #
    # when `digits` is empty, return a list of one empty string
    
    # when `len(digits)` >= 1, we list out the characters represented by `digits[0]`:
    #  
    # a1, a2, a3,
    
    # and recursively find the solutions for input `digits[1:]`:
    # 
    # s1, s2, s3, ..., sn
    
    # We simply enumerate all the combination between 
    
    # a1, a2, a3
    #
    # and 
    # 
    # s1, s2, s3, ..., sn
    d2c = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
    }
    return self.recursion(digits, d2c)  
      
      
  def recursion(self, digits, d2c):      
    if len(digits) == 0:
      return ['']
    
    letters = d2c[digits[0]]
    combinations = self.recursion(digits[1:], d2c)
    
    result = []
    for char in letters:
      for comb in combinations:
        result.append(char + comb)
    return result    
