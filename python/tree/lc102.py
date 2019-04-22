"""102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
      return []
    
    # The idea: 
    
    # Use two lists `curr_level` and `next_level` to keep track of the nodes
    # in current level and next level
    
    # At the beginning of iteration:
    
    
    #     3         <== curr_level = [3]              vals = []
    #    / \
    #   9  20       <== next_level = []
    #     /  \
    #    15   7
    
    # At the end of iteration
    
    #     3                                           vals = [3]        
    #    / \
    #   9  20       <== curr_level = [9, 20]
    #     /  \
    #    15   7     <== next_level = []
    
    # nodes in `curr_level` are listed in left-to-right order
    # We traverse them and put their non-empty children to `next_level`, which 
    # are exactly those nodes in the next level
      
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
      # `next_level` becomes current level in the next iteration
      curr_level = next_level
      next_level = [] # reset `next_level` to empty list
      
    return levels  
