"""40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution(object):
  def combinationSum2(self, candidates, target):
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
      
      
      # NOTE: if `nums[i]` is the same as previous value `nums[i - 1]`, then
      # all possible combinations that sum up to `target`, using numbers from
      # `nums[i - 1]`, `nums[i]`, ... `nums[-1]` must have already been found
      # in the previous iteration `i` - 1.
      
      # If were to proceed with this iteration `i`, we would have the same target
      # `target` - `nums[i]` == `target` - `nums[i - 1]` as in the previous iteration.
      
      # Although we have a different set of candidates to pick from, i.e. starting 
      # now from `nums[i]` up to `nums[-1]` rather than `nums[i - 1]`, we would find
      # duplicate combinations.
      
      # So we have to skip this iteration, until we find a strictly LARGER value
      # in `nums`
      if i > start and nums[i - 1] == nums[i]:
        continue
      
      if target - nums[i] >= 0:
        # NOTE: The next number we pick can't be `nums[i]`, since all numbers 
        # can only be picked ONCE. 
        all_but_i = self.recursion(nums, target - nums[i], i + 1)       
        
        
        # `all_but_i` holds ALL possible combinations that sum up to
        # `target` - `nums[i]`, and the minimum number in each combination
        # is `nums[i]`
        
        for combination in all_but_i:
          result.append([nums[i]] + combination)
        # Inductive assumption maintained:  
          
        # Now the combinations in `result` start with `nums[i]`, and are 
        # sorted in non-decreasing order, and sums up to `target`
        
    return result      
