"""80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    
    # The idea:
    
    # LOOP INVARIANT:

    # at any point, 
    # 
    # the prefix
    # nums[0], ..., nums[i] contains non-decreassing numbers, where each number 
    # appears at most twice.
    # and `count` is the nubmer of times that `nums[i]` appears in the prefix

    # In each iteration, we read a number `nums[j]` and we do one of the two
    # things:
    
    # 1. if nums[j] == nums[i]
    #       if count == 1
    #           we simply increment `count`, and place `nums[j]` after `nums[i]`
    #       if count == 2
    #           we need to skip the current number `nums[j]`, until we see a 
    #           strictly larger number
    
    # 2. if nums[j] != nums[i]
    #
    #   we simple reset `count`, and place `nums[j]` after `nums[i]`    
    i, count = 0, 1
    for j in range(1, len(nums)):
      if nums[j] == nums[i]:
        if count == 1:
          i += 1
          nums[i] = nums[j]          
          count += 1
      else:
        i += 1
        nums[i] = nums[j]
        count = 1
    return i + 1    
          
    
