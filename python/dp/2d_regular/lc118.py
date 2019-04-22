"""118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
class Solution(object):
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
      return []
    
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
    pascal = [[1]]
    # initialize current row
    curr = [1]
    
    for i in range(1, numRows):
      # at the beginning of each iteration, 
      # current row always starts with 1
      # and has the same length as previous row `prev`
    
      # previous row
      prev = pascal[i - 1]
          
      # we only update internal elements in `curr`
      for j in range(1, len(prev)):
        curr[j] = prev[j] + prev[j - 1]
        
      # append 1 to current row, now it has one more element than
      # prevous row
      curr.append(1)
      # make copy of `curr`
      pascal.append(list(curr))
      
    return pascal  
