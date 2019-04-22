"""128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """    
    # We want to find the longest consecutive sequence.
    #
    # So when reading a new number `nums[i]`, which is by itself a length-1 consecutive 
    # sequence. 
    
    # We would want to extend it in either or both directions 
    #                         
    #                        <==                       ==>   
    #                       nums[i] - 1, nums[i], nums[i] + 1
    #                       ?            current  ?     
    #
    #
    # If `nums[i]` - 1 has been already recorded, and if we know the length of the longest
    # consecutive sequence that `nums[i]` - 1 is part of, we could easily extend the
    # current length-1 sequence -- `nums[i]` -- in the left direction. 
    #
    # We can do the same if `nums[i]` + 1 has already been recorded.
    
    
    # `cons_seq_len` maps the each number in `nums` to the length of the longest consecutive
    # sequence that this number is part of.
    #
    # For example, after reading [100, 4, 200, 1, 3], `cons_seq_len` becomes
    # { 100:  1         # singleton
    #   200:  1         # singleton 
    #   1:    1         # singleton
    #   3:    2         # part of sequence [3, 4]  
    #   4:    2 }       # part of sequence [3, 4]
    #
    # We read numbers in `nums` one at a time,
    # upon reading `nums[i]`, we must update `cons_seq_len` accordingly:
    #
    #
    #   
    #  <-- left consecutive seqeunce, len = `l`-->          <-- right consecutive seqeunce, len = `r` -->
    #  nums[i] - l,  ...    ,          nums[i] - 1, nums[i], nums[i] + 1,    ...,             nums[i] + r     
    #                                              ^        
    

    # If `l` > 0, then we DO have a left consecutive sequence
    #
    # and it can be extended by 1 + 'r' (i.e. `nums[i]` and the right consecutive sequence)
    #
    # And we MUST update the left end of the extended consecutive sequence
    #
    #   `nums[i] - l` now maps to `l + r + 1` instead of `l`
    
    # Similarly, if `r` > 0, the we DO have aright consecutive sequence
    
    # We MUST update the right end of the extended consecutive sequence
    #
    #   `nums[i] + r` now maps to `l + r + 1` instead of `r`
    
    # NOTE, it would be sufficient to ONLY update the endpoints of a consecutive sequence.
    
    longest = 0
    cons_seq_len = {}
    for i in range(len(nums)):
      if nums[i] not in cons_seq_len:
        left = cons_seq_len.get(nums[i] - 1, 0)
        right = cons_seq_len.get(nums[i] + 1, 0)

        seq_len = left + right + 1
        # update `cons_seq_len[nums[i]]`
        cons_seq_len[nums[i]] = seq_len
        longest = max(longest, seq_len)
        
        if left > 0:
          # update the left endpoint
          cons_seq_len[nums[i] - left] += right + 1
        if right > 0:
          # update the right endpoint
          cons_seq_len[nums[i] + right] += left + 1
    return longest
