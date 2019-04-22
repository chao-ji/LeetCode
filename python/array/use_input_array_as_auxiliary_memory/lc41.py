"""41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
# Solution 1
# use O(n) space
class Solution(object):
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # given an array `nums` of size `n`, the first missing positive 
    # must be in the range [1, n + 1] (inclusive)
    # 1, if None of elements in `nums` are positive
    # n + 1, if elements in `nums` are 1, 2, ..., n
    n = len(nums)
    # `mark[i]` indicates the existence of `i`, where 1 <= `i` <= n 
    mark = [False for _ in range(n + 2)]
    # we scan `nums` to mark the existence of `nums[i]`
    for i in range(len(nums)):
      if nums[i] >= 1 and nums[i] <= n + 1:
        mark[nums[i]] = True
    # return the first unmarked `i`     
    for i in range(1, n + 2):
      if not mark[i]:
        return i

# Solution 2
# use O(1) space
class Solution(object):
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Given array `nums` of size `n`, the first missing positive integer
    # must be in the range [1, n] or n + 1
    # 
    # Ideally, we want each integer `nums[i]` that is in the range [1, n]
    # to be placed at index `nums[i] - 1`, e.g.
    
    # nums[i]   1 2 3 4 5 6
    # i         0 1 2 3 4 5
    
    # We start from index `i`, and swap `nums[i]` with `nums[nums[i] - 1]` --
    # `nums[i] - 1` is the right index for `nums[i]`, only if these two numbers
    # are different.
    
    # This way in each iteration we move one `nums[i]` to its correct index
    # `nums[i] - 1`
    i = 0
    while i < len(nums):
      if (nums[i] >= 1 and nums[i] <= len(nums) and 
          nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]):
        tmp = nums[nums[i] - 1]
        nums[nums[i] - 1] = nums[i]
        nums[i] = tmp
      else:
        i += 1
    
    # return the first number `nums[i]` that is not `i + 1`
    for i in range(len(nums)):
      if nums[i] != i + 1:
        return i + 1
    # `nums` contains all numbers in [1, n], return n + 1  
    return len(nums) + 1  



# Follow up question: Find first missing even number

# even nubmers are defined as 2, 4, 6, 8 ...

# Claim: first missing even number must be even number in [2, len(nums) * 2 + 2]

import numpy as np

def first_missing_even(nums): 
  i = 0
  while i < len(nums):
    if (nums[i] >= 2 and              # in range
        nums[i] <= len(nums) * 2 and  # in range
        nums[i] % 2 == 0 and          # even number
        nums[i] != 2 * i + 2 and      # correct number at index `2 * i + 2`
        nums[(nums[i] - 2) // 2] != nums[i]): # correct index for number `nums[i]`

      tmp = nums[(nums[i] - 2) // 2]
      nums[(nums[i] - 2) // 2] = nums[i]
      nums[i] = tmp
    else:
      i += 1

  print(nums) 
  for i in range(len(nums)):
    if nums[i] != 2 * i + 2:
      return 2 * i + 2

  return len(nums) * 2 + 2

