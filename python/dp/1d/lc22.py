"""22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# Solution 1, DP
class Solution(object):
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    # See LC 95, 96 Unique Binary Search Trees (I and II)
    
    # The idea:
    
    # Any well-formed set of parentheses must START with a '(' and has the pairing ')'
    
    # somewhere to the right of starting '(':
    
    
    #   ([`m` well-formed parentheses])[`n` - `m` - 1 well-formed parentheses]
    #   ^
    #   0
    
    # The space between the '(' and ')', as well as the space to the right of ')', 
    # must also be well-formed parentheses.
    
    # If we are given `n` total pairs of parentheses, then we can allocate `m` >= 0
    # to the space between '(' and ')', and `n` - `m` - 1 to the right of ')'.
    
    # So it can be done recursively. But it has OVERLAPPING subproblems:
    
    # `n` pairs well-formed parentheses can be at different locations.
    
    # We can use dynammic programming.
    
    
    
    # `dp[i]` stores the list of `i` pairs of well-formed parenthesis, i >= 0
    dp = []
    
    # Base case:
    # `dp[0]` = [empty string]
    dp.append([""])
    
    for i in range(1, n + 1):
      sols = []
      # we enumerate the combination of allocating `j` and `i` - `j` - 1 parentheses
      # in between and to the right of '(' and ')'
      for j in range(i):
        sols.extend(["(" + l + ")" + r for l in dp[j] for r in dp[i - 1 - j]])
      dp.append(sols)  
        
    return dp[n]

# Solution 2, backtrack
class Solution(object):
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    solutions = []
    self.backtrack([], solutions, 0, 0, n)
    return solutions
  
    # The idea: use backtracking
    
    # We can grow the sequence of '(' and ')' one at a time, but with the
    # following constraints:
    
    # 1. The sequence must start with '('.
    # 2. At any time, the number of '(' must <= `n`
    # 3. At any time, the number of ')' must < '('
    # 4. The total number of '(' and ')' must <= '2n'
  
    # As we grow the sequence, we can choose to do either of the two things:
    
    # 1. Add a '(', as long as the count of '(' < `n`
    # 2. Add a ')', as long as the count of '(' > the count of ')'
  def backtrack(self, solution, solutions, left, right, n):
    """
    `solution` is a growing list of '(' and ')' that can be potentially
      completed as a valid set of parentheses.
    `left`: count of '(' in `solution`.
    `right`: count of ')' in `solution`
    """    
    # The solution can still be grown
    # `solution` is a partially valid sequence of parentheses
    if len(solution) < n * 2:
      # as long as count of '(' < `n`, we can place one more '('
      if left < n:
        solution.append('(')
        left += 1
        self.backtrack(solution, solutions, left, right, n)
        left -= 1
        solution.pop()
     
      # Or we can add one more ')', as long as there are more '(' than ')'
      if right < left:
        solution.append(')')
        right += 1
        self.backtrack(solution, solutions, left, right, n)
        right -= 1
        solution.pop()
      # BACKTRACK
      return 
    
    # solution is complete
    solutions.append(''.join(solution))
        
