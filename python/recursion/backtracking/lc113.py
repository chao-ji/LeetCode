"""113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
      return []
    
    solutions = []
    self.search([root], solutions, root.val, sum) 
    return solutions

    # Intuition: staightforward to use Backtracking

    # We start with a partial solution (i.e. a path from root to a non-leaf node),
    # and want to extend until is complete:

    # Grow solution: 
    #
    #      [root]   ====>  [root, node1]  ==>  [root, node1, ..., leaf],  a full root-to-leaf path!

    # When growing the partial solution, we make choices out of a fixed number (i.e. extend
    # the root-to-leaf path into the left or right subtree) of options. Some choices would 
    # eventually lead us to the final complete solution (i.e. sum == target), while others may 
    # take us to dead ends (i.e. sum != target)

    # If the goal is to find ALL valid solutions, 
    # then whenever we have a complete solution, or we hit a dead end -- 
    # it means we can no longer grow the current solution.

    # we backtrack -- we return to the calling function, and proceed with the next option.    
  
  def search(self, solution, solutions, running_sum, sum):
    # solution: a list of nodes in the root-to-leaf path,
    # running_sum: the sum of values of nodes in `solution`.
    
    # the solution (i.e. the root-to-leaf path) can still be extended:
    #
    # path is empty or last of of path is not leaf
    if not solution or solution[-1].left or solution[-1].right:
      
      # last node of the path
      root = solution[-1]
      
      if root.left:
        solution.append(root.left)
        running_sum += root.left.val
        self.search(solution, solutions, running_sum, sum)
        running_sum -= root.left.val
        solution.pop()
        
      if root.right:
        solution.append(root.right)
        running_sum += root.right.val
        self.search(solution, solutions, running_sum, sum)
        running_sum -= root.right.val
        solution.pop()
      
      # BACKTRACK
      return
    
    # solution can't be extended, test if it is valid
    if running_sum == sum:  
      solutions.append([n.val for n in solution])   
