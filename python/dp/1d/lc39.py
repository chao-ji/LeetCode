"""39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
# Solution 1
# DP
# O(NT^2): `N`: number of coins, `T`: target

class Solution(object):
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # Intuition: Dynamic Programming
    
    # Typicall Knapsack/coin change problem. 
    
    # 1. Unlimited supply in each denomination 
    # 2. Unlimited total number of coins
    # 3. Results must be COMBINATIONS rather than PERMUTATION, 
    #   so 1, 1, 2 == 1, 2, 1
    
    
    # Since duplicate combinations are not allowed, we can incrementally expand
    # our set of coins.
    
    # For `candidates[:j]`, we update `dp[1]`, ..., `dp[target]` using the additional
    # coin `candidates[j - 1]` that becomes available.
    
    
    # `dp[i]` = list of combinations (list) of numbers that add up to `i`
    dp = [[] for _ in range(target + 1)]
    # `dp[0]` = list of empty list
    dp[0] = [[]]
    
    for j in range(len(candidates)):
      # Loop invariant: 
      # At the start of each OUTER for loop, `dp[1]`, ..., `dp[target]` each contains
      # the list of combinations that add up to 1, ..., `target`, using coins in the 
      # set `candidates[:j]` (i.e. not including the current coin `candidates[j]`)
      for i in range(1, target + 1):
        if i >= candidates[j]:
          dp[i].extend([combination + [candidates[j]] for combination in dp[i - candidates[j]]])
      
      # At the each of each OUTER for loop, `dp[1]`, ..., `dp[target]` have been 
      # updated to include the combinations that uses the newly available coin 
      # `candidates[j]`
      
    return dp[-1]

# Solution 2
# Recursion
class Solution(object):
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates = sorted(candidates)
    return self.recursion(candidates, target, 0)
    # Intuition:
  
    # We pick a number `a` from `candidates`, then we are left with a SMALLER problem:
    #
    # find combinations that sums up to `target` - `a`,
    
    # until we hit the BASE CASE:
    # when `target` == 0, we simple return empty set []
    
    
    # We sort numbers in `candidates` in non-decreasing order, and recursively find
    # the DISJOINT groups of combinations that sum to `target`:
    
    # the combinations with `candidates[0]` as the minimum
    # the combinations with `candidates[1]` as the minimum
    # ...
    # the combinations with `candidates[-1]` as the minimum
    
  def recursion(self, nums, target, start):
    """Returns all distinct combinations of numbers picked from 
    [nums[start], ..., nums[-1]] that sum to `target`
    
    Inductive assumption:
    1. the numbers in each combination must sum to `target`.
    2. the result contains ALL possible combinations.     
    3. numbers in each combination are sorted in non-decreasing order
    """
    # Base case:
    # there is only one combination -- empty set -- that sums to 0.
    if target == 0:
      return [[]]
      
    result = []  

    for i in range(start, len(nums)):
      # In each iteration, we find all the combinations that start with
      # `nums[i]`, which sums up to `target`
      
      if target - nums[i] >= 0:
        all_but_i = self.recursion(nums, target - nums[i], i)       
        # `all_but_i` holds ALL possible combinations that sum up to
        # `target` - `nums[i]`, and the minimum number in each combination
        # is `nums[i]`
        
        for combination in all_but_i:
          result.append([nums[i]] + combination)
        # Inductive assumption maintained:  
          
        # Now the combinations in `result` start with `nums[i]`, and are 
        # sorted in non-decreasing order, and sums up to `target`
        
    return result       
