"""20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
"""
class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
      return True
    
    # ASSUME `s` is made of chars ONLY in '()[]{}'
    
    # The idea: use stack, 
    
    # LOOP INVARIANT: We ONLY PUSH LEFT parentheses: ( [ { onto stack
    
    # At any time, if we see a right parenthesis: ) ] }, there must be a left
    # parenthesis already at the top of stack. If stack is empty, we return False.
    
    # We compare the right parenthesis with character at the top of the stack, if 
    # not match, we return False; otherwise we pop the stack and proceed with 
    # next character in `s`.
    
    # At the end, we must have matched up all the left-right parentheses, the stack
    # is supposed to be empty. Otherwise we return False.
    
    stack = []
    # In each iteration, we will always consume a char in `s`, we either
    # 1. push a left parenthesis onto stack,
    # 2. or, cancel it out with the matching parenthesis at the top of stack.
    for c in s:
      if c in "([{":
        stack.append(c)
      else:   # c must be in ")]}"
        if not stack:
          return False
        
        # `left` must be a left parenthesis
        left = stack.pop()
        if not self.match(left, c):
          return False
    
    return not stack
  
  def match(self, ci, cj):
    return (ci == '(' and cj == ')' or 
            ci == '[' and cj == ']' or 
            ci == '{' and cj == '}')
