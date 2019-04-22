"""216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution(object):
  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    return self.recursion(k, n, 1)
  
    # Intuition:
  
    # We pick a number `a` from [1, 9], then we are left with a SMALLER problem:
    #
    # find combinations starting from `a` + 1 that sums up to `n` - `a`, 
    # using `k` - 1 numbers
    
    # until we hit the BASE CASE:
    # when `n` == 0 and `k` == 0, we simple return empty set []
    
    # So each subproblem is parameterized by
    # 1. size: how many numbers to pick from 1, 2, ..., 9
    # 2. target: the target sum
    # 3. start: we pick numbers from `start`, `start` + 1, ..., 9
  
  def recursion(self, size, target, start):
    """Return all distinct combinations of `size` numbers picked from 
    start, start + 1, 9 that sum to `target`
    
    Inductive assumption:
    1. the numbers in each combination must sum to `target`.
    2. the size of combination is `size`   
    3. numbers in each combination are sorted in non-decreasing order  
    
    
    Args:
      size: int scalar >= 0
      target: int scalar >= 0
      start: int scalar, 1, 2... 9
    """
    # Base case:
    if target == 0 and size == 0:
      return [[]]
    
    result = []
    for i in range(start, 10):
      if target - i >= 0 and size - 1 >= 0:
        all_but_i = self.recursion(size - 1, target - i, i + 1)
        # 1. all the combinations in `all_but_i` has size `size` - 1
        # 2. and sums up to `target` - `i`,
        # 3. and the minimum number in each combination is `i` + 1
        for combination in all_but_i:
          result.append([i] + combination)
        # inductive assumption maintained:
        
        # Adding back the number `i`,
        # 1. all the combinations in `result` has size `size`,
        # 2. and sums up to `target`
        # 3. and the minimum number in each combination is `i`
    return result       
