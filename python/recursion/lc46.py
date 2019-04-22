"""46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return self.recursion(nums)
    
  # KEY idea:
  
  # The number of permutations of a sequence of size `n` must be `n!`, if the sequence
  # contains unique elements; or it will be less than `n!`, if the sequence contains 
  # duplicate elements.
  
  
  
  # To generate a permutation from a sequence, we need to pick numbers one at a time,
  # WITHOUT replacement, until we have picked everything.
  
  # The generated permutation would be:
  
  # 1st num picked, 2nd num picked, ..., last num picked.
  
  # Suppose we have a sequence: nums[0], nums[1], ..., nums[-1], to pick numbers from.
  
  # and we picked `nums[i]` as the 1st number in the permutation sequence, then we're left
  # with a SMALLER problem: generating all unique permutations of sequence:
  
  # nums[0], ..., nums[i - 1], nums[i + 1], ..., nums[-1]
  
  # And we will extend `nums[i]` with each unique permutation sequence generated from the 
  # smaller sequence.
    
  
  def recursion(self, nums):
    # Base case:
    # empty sequence has only one permutation: []
    if not nums:
      return [[]]
        
    result = []
    
    for i in range(len(nums)):
      # In each iteration, we pick `nums[i]`, and we are left with smaller sequence
      # `nums[:i]` + `nums[i + 1:]`, for which we will recursively find the all the unique
      # permutation sequences. And finally put together the permutation sequence of the 
      # full problem.

      all_but_i = self.recursion(nums[:i] + nums[i + 1:])    
      for permutation in all_but_i:
        result.append([nums[i]] + permutation)
          
    return result        
        
