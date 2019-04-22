"""77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    # Assume input is always valid:
    # 1 <= k <= n
  
    # The idea: it's straightforward to use recursion
  
    # The size of each problem is characterized by `k`. Base cases are
    # when `k` == 1, i.e., we have no choice but to pick each item from
    # 1, 2, ..., n
    
    # Recursion:
    
    # To choose `k` numbers from 1, 2, ..., n, we can
    
    # 1. Choose `k` numbers from 1, 2, ..., n - 1
    # 2. Choose `k` - 1 numbers from 1, 2, ..., n - 1, and then for each
    #   combination, add the new number `n`
  
    # Base case:
    if k == 1:
      return [[i] for i in range(1, n + 1)]
    
    # holding all combinations:  
    result = []

    
    # Recursion, option 1
    if n - 1 >= k:  
      without_n = self.combine(n - 1, k)
    else:
      without_n = []
    
    # Recursion, option 2
    with_n = self.combine(n - 1, k - 1)   
    for combination in with_n:
      result.append(combination + [n])
      
    # combine option 1 and 2  
    result.extend(without_n)
    return result
