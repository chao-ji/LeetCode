"""89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""
class Solution(object):
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    solutions = []
    self.gray([0], solutions, n, 1)
    return solutions[0]

    # Intuition: staightforward to use Backtracking

    # We start with a partial solution (i.e. partial gray code sequence), and want to extend 
    # until is complete:

    # Grow solution: 
    #
    #      [0]   ====>  [0, 1]  ==>  [0, 1, 3, 2],  complete gray code sequence !

    # When growing the partial solution, we make choices out of a fixed number (i.e. `k`) of
    # options. Some choices would eventually lead us to the final complete solution, while
    # others may take us to dead ends

    # If the goal is to find ALL valid solutions, 
    # then whenever we have a complete solution, or we hit a dead end -- 
    # it means we can no longer grow the current solution.

    # we backtrack -- we return to the calling function, and proceed with the next option.  
  
  def gray(self, solution, solutions, n, num_sols):
    if len(solutions) < num_sols:
      if len(solution) < 2**n:
        for i in range(n):
          next_val = self.flipBit(solution[-1], i)
          if next_val not in solution:
            solution.append(next_val)
            self.gray(solution, solutions, n, num_sols)
            solution.pop()
        # BACKTRACK: 
        # Invalid solution
        return 
      solutions.append(list(solution))  
      # BACKTRACK (implicit):
      # Final complete solution
        
  def flipBit(self, num, bit):
    mask = 1 << bit
    return num ^ mask
