"""90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
  def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)    
    
    return self.recursion(nums)
  
  # KEY idea:
  
  # The number of subsets of a set of size `n` must be `2^n`, if the set
  # contains unique elements; or it will be less than `2^n`, if the set contains
  # duplicate elements -- the set is a MULTI-set.
  
  
  # Assumption: numbers in `nums` are sorted in non-decreasing order.
  
  # Now we are to generate subsets of set
  #
  # S = {nums[0], ..., nums[-2], nums[-1]}, i.e., pow(S), 
  
  # given that we already have UNIQUE subsets of set 
  # S' = {nums[0], ..., nums[-2]}, i.e., pow(S')
  # 
  
  # Note that subsets in `pow(s)` can be divided into two DISJOINT groups:
  
  # group A. those that contain the element `nums[-1]`
  #
  # group B. those that do not contain the element `nums[-1]`
  
  
  
  
  # We need to consider whether the new number `nums[-1]` is already 
  # present in `S'` or not.
  
  # Case 1: the new number `nums[-1]` > `nums[-2]`, 
  #
  # In this case, `pow(S)` can be built by extending every set in 
  # `pow(S')` with the new number `nums[-1]`, i.e. group A, as well as 
  # including every set in `pow(S')` themselves WITHOUT the new number 
  # `nums[-1]`, i.e. group B.
  
  # Case 2: the new number `nums[-1]` == `nums[-2]`
  #
  # In this case, group B is those subsets in `pow(S')` that do not contain
  # the element `nums[-1]`, i.e. empty set [], and subsets whose last element
  # is not equal to `nums[-1]`.
  #
  # To build group A, we only need to increase the MULTIPLICITY (i.e. count) of 
  # `nums[-1]` in each set of `pow(S')` by appending the new number `nums[-1]`.
  
  # Example:
  # S: nums = [1, 2, 2]
  
  # S1: nums[:-1], or [1, 2]
  # pow(S'):
  # { 
  #   []
  #   [1]
  #   [2]
  #   [1,2]
  # }   

  # group A, appending 2 to each set in `pow(S')`
  # {
  #   [2]
  #   [1,2]
  #   [2,2]
  #   [1,2,2]
  
  # group B, those that do not have 2
  #   []
  #   [1]
  # }
        
  def recursion(self, nums):
    """Generate all unique multi-subsets of a multi-set represented 
    as a list of numbers.
    
    Args:
      nums: a list of ints, of non-decreasing values. The multi-set.
      
    Returns: 
      all unique multi-subsets of `nums`, each multi-subset is represented 
      as a list of non-decreassing numbers.
    """
    # Base case:
    # empty set has only one subset: empty set
    if not nums:
      return [[]]
           
    result = []  
    # pow(S'): unique subsets of `nums[:-1]` 
    without_last = self.recursion(nums[:-1])
    
    # group B: increasing the multiplicity of `nums[-1]`
    for subset in without_last:
      result.append(subset + [nums[-1]])
    # group A: include only those that do not have `nums[-1]`   
    for subset in without_last:
      if not subset or subset[-1] != nums[-1]:
        result.append(subset)
    return result
