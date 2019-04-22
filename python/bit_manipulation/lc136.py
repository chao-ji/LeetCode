"""136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""
# Solution 1
# Bit manipulation, O(n)
class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # We do bitwise XOR, which is associative and commutative
    # No matter what order the numbers in `nums` come,
    # Those that appear twice will cancel out each other, and the singleton
    # will be left as the answer
    v = nums[0]
    for i in range(1, len(nums)):
      v = v ^ nums[i]
      
    return v  

# Solution 2
# Hash table, O(n)
class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Use a set to keep track of numbers that we have seen
    # 
    # If a new number is found, add to set
    # otherwise, delete it from set
    # 
    # The singleton, will be added to set and never been deleted.
    s = set()
    for i in range(len(nums)):
      if nums[i] not in s:
        s.add(nums[i])
      else:
        s.remove(nums[i])
    return list(s)[0]
