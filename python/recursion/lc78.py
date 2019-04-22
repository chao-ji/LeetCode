"""78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return self.recursion(nums)
  
  # KEY idea:

  # The number of subsets of a set of size `n` must be `2^n`, if the set
  # contains unique elements; or it will be less than `2^n`, if the set contains
  # duplicate elements -- the set is a MULTI-set.


  
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

  

  # `pow(S)` can be built by extending every set in 
  # `pow(S')` with the new number `nums[-1]`, i.e. group A, as well as 
  # including every set in `pow(S')` themselves WITHOUT the new number 
  # `nums[-1]`, i.e. group B.


  # Example:
  # S: nums = [1, 2, 3]

  # S1: nums[:-1], or [1, 2]
  # pow(S'):
  # { 
  #   []
  #   [1]
  #   [2]
  #   [1,2]
  # }   

  # group A, appending 3 to each set in `pow(S')`
  # {
  #   [3]
  #   [1,3]
  #   [2,3]
  #   [1,2,3]

  # group B, those that do not have 3
  #   []
  #   [1]
  #   [2]
  #   [1,2]
  # }
  
    
  def recursion(self, nums):
    """Generate all unique subsets of a set represented 
    as a list of numbers.
    
    Args:
      nums: a list of ints, of unique values. The set of numbers.
      
    Returns: 
      all unique subsets of `nums`, each subset is represented 
      as a list of unique numbers.
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
        result.append(subset)
    return result

      
