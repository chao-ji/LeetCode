"""95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
      return []
    
    # The idea:
    #
    # Given numbers 1, 2, ..., n
    # We can choose to put each of them at the root,
    
    # Say we choose to put `i` the the root, we are left with 
  
    # 1, 2, ..., `i` - 1, which we can put in the left subtree,
    #
    # `i` + 1, ..., `n` - 1, `n`, which we can put in the right subtree.
    
    # Each of the two subproblems can be solved recursively.
    #
    # Since left and right subtree do not share any number in common,
    #
    # There is no overlapping subproblem. We just do recursion.
    
    # Each subproblem is characterized by the starting and ending number
    
    # Initially we call func(1, n)
    
    return self.generate(1, n)

  def generate(self, start, end):
    if start > end:
      return [None]
    
    trees = []
    for i in range(start, end + 1):
      left_tree = self.generate(start, i - 1)
      right_tree = self.generate(i + 1, end)
      for l in left_tree:
        for r in right_tree:
          root = TreeNode(i)
          root.left = l
          root.right = r
          trees.append(root)
    return trees      
