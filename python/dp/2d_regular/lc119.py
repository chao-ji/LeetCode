"""119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
  def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # The idea: straightforward to use DP
    
    #    Pascal Triangle looks like:
    
    #                 1
    #               1   1
    #             1   2   1
    #           1   3   3   1
    #         1   4   6   4   1
    #       ...   ...     ...   ...
    
    # Except for the first and last element in each row, internal elements
    # are computed as `curr_row[i]` = `prev_row[i - 1]` + `prev_row[i]`    
    
    # Base case:
    # first row of Pascal Triangle
    prev_row = [1] 
    
    # allocate memory for current row
    curr_row = [1]
    
    # NOTE: we only allocate memory once upfront for `prev_row` and `curr_row`,
    # and each of them grow by one element at a time in each iteration.
    # So it uses O(n) memory.
  
    for i in range(1, rowIndex + 1):
      # `i` is the index of the current row
      
      # at the beginning of each iteration, 
      # current row always starts with 1
      # and has the same length as previous row `prev_row`
      
      # we only update internal elements in `currrow`
      for j in range(1, len(prev_row)):
        curr_row[j] = prev_row[j] + prev_row[j - 1]
      
      # append 1 to current row, now it has one more element than
      # prevous row
      curr_row.append(1)  
      
      # copy the content of `prev_row` to `prev_row`
      for j in range(len(prev_row)):
        prev_row[j] = curr_row[j]
      prev_row.append(1)  
      # at this point `prev_row` has the same content as `curr_row`,
      # though residing in different memory space
    
    return prev_row
