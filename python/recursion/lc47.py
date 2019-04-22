"""47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
  def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    return self.recursion(nums)
    
  # KEY idea:
  
  # The number of permutations of a sequence of size `n` must be `n!`, if the sequence
  # contains unique elements; or it will be less than `n!`, if the sequence contains 
  # duplicate elements.
  
  # Assumption: numbers in `nums` are sorted in non-decreasing order.
  
  
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
  
  
  # Dealing with DUPLICATES:
  
  # As opposed to LC 46, since numbers in `nums` may have duplicates, we need to be careful
  # about which number we can pick:
  
  # Suppose we have
  
  # nums[0] < ... < nums[j] == nums[j + 1] < ... < nums[-1], i.e. numbers sorted in 
  
  # non-decreasing order.
  
  # After we picked `nums[j]`, we are left with a smaller sequence. BUT, if we picked 
  
  # `nums[j + 1]`, we would be left with the SAME smaller sequence, which would eventually
  
  # generate the same permutations sequences. This is what we must avoid.
  
  
  # Example:
  # nums: [1, 1, 2]

  # we 1st picked 1, and we are left with 1, 2, which have permutation sequences
  # 1, 2 and 2, 1
  #
  # so we have 1, 1, 2 and 1, 2, 1

  # we need to SKIP the second 1, and pick 2, and we are left with 1, 1, which have one 
  # permutation sequence 1, 1
  # so we have 2, 1, 1

  
  def recursion(self, nums):
    # Base case:
    # empty sequence has only one permutation: []
    if not nums:
      return [[]]
    
    # NOTE: numbers in `nums` must be sorted in non-decreasing order.
    
    result = []
    
    for i in range(len(nums)):
      # In each iteration, we pick `nums[i]`, and we are left with smaller sequence
      # `nums[:i]` + `nums[i + 1:]`, for which we will recursively find the all the unique
      # permutation sequences. And finally put together the permutation sequence of the 
      # full problem.

      # The ONLY exception: we must avoid picking two consecutive numbers that are the same: 
      if i == 0 or nums[i - 1] != nums[i]:
        all_but_i = self.recursion(nums[:i] + nums[i + 1:])    
        for permutation in all_but_i:
          result.append([nums[i]] + permutation)
          
    return result        
        
