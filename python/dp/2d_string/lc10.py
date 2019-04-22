"""10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    ls, lp = len(s), len(p)
    
    # `match[i][j]` stores whether `s[:i]` matches `p[:j]`
    match = [[False for j in range(lp + 1)] for i in range(ls + 1)]
    # empty string matches empty pattern
    match[0][0] = True
    
    # match
    # [0][0]  [0][1]  ...   [0][lp]
    # [1][0]  [1][1]  ...   [1][lp]
    # ...     ...     ...   ...
    # [ls][0] [ls][1] ...   [ls][lp]
    
    # The first col corresponds to empty pattern, and first row corresponds to empty string
    
    # The first col except [0][0] is initialized to False -- non-empty string doesn't match empty pattern
    
    # The initial value of first row depends on the '[c]*' in pattern string:
    # If the pattern string has '*' at index `j - 1`, then it matches the empty string as long as `p[:j - 2]`
    # matches the empty string
    for j in range(2, lp + 1):
      if p[j - 1] == '*':
        match[0][j] = match[0][j - 2]
        
    for i in range(1, ls + 1):
      for j in range(1, lp + 1):
        # `s_char` the current char in string
        # `p_char` the current char in pattern
        s_char, p_char = s[i - 1], p[j - 1]
        
        
        # pattern:   `p[:j-2]`, [c],  p_char
        #                       j-2   j-1 
        #
        # string:     `s[:i-1]`,      s_char
        #                             i-1
        #
        # If `p_char` is not '*',
        #   then `p_char` has to match `s_char`, and `p[:j - 1]` has to match `s[:i - 1]`
        #
        # If `p_char` is *,
        #   then we have two options:
        #     1. `s[:i]` matches `p[:j - 2]` -- we don't need the '[c]*' at the end of pattern
        #     2. `s[:i - 1]` matches `p[:j]` and `s[i - 1]` matches the '[c]' preceding '*'
        if p_char == '*':
          t_char = p[j - 2]
          match[i][j] = (match[i][j - 2] or                                         # option 1
                         (match[i - 1][j] and (s_char == t_char or t_char == '.'))) # option 2
        else:
          match[i][j] = ((s_char == p_char or p_char == '.')  # `s_char` matches `p_char`
                         and match[i - 1][j - 1])             # s[i - 1:] matches `p[j - 1:]`
    return match[ls][lp]  


# Follow up
# Support '?' and '+'
def regexp(s, p):
  """

  '.' matches any single character.
  '*' matches zero or more of the preceding element.
  '?' matches zero or one of the preceding element.
  '+' matches one or more of the preceding element.

  Args:
    `s`: str scalar, string to be matched.
    `p`: str scalar, a valid pattern string.
  """

  ls, lp = len(s), len(p)

  match = [[False for j in range(lp + 1)] for i in range(ls + 1)]
  match[0][0] = True

  for j in range(2, lp + 1):
    if p[j - 1] == '*' or p[j - 1] == '?':
      match[0][j] = match[0][j - 2]


  for i in range(1, ls + 1):
    for j in range(1, lp + 1):
      s_char, p_char = s[i - 1], p[j - 1]

      if p_char == '*':
        t_char = p[j - 2]
        match[i][j] = match[i][j - 2] or ((s_char == t_char or t_char == '.') and match[i - 1][j])

      elif p_char == '?':
        t_char = p[j - 2]
        match[i][j] = match[i][j - 2] or ((s_char == t_char or t_char == '.') and match[i - 1][j - 2])

      elif p_char == '+':
        t_char = p[j - 2]
        match[i][j] = (s_char == t_char or t_char == '.') and (match[i - 1][j] or match[i - 1][j - 2])

      else:
        match[i][j] = (s_char == p_char or p_char == '.') and match[i - 1][j - 1]

  return match[ls][lp]
 
