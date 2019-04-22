"""107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
      return []
    
    # Exactly the same as LC 102 Binary Tree Level Order Traversal II
    # The only difference is to reverse the list of per-level sequences
    curr_level = [root]
    next_level = []
    levels = []
    
    while curr_level:
      vals = []
      for node in curr_level:
        vals.append(node.val)
        if node.left:
          next_level.append(node.left)
        if node.right:
          next_level.append(node.right)
          
      levels.append(vals)    
      curr_level = next_level    
      next_level = []
    
    # reverse the list of per-level sequences
    return reversed(levels)  
