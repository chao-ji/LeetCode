"""103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
      return []
    # Exactly the same as LC 102 Binary Tree Level Order Traversal
    # The only difference is to reverse per-level sequence in every other level.
    
    # ===>  l2r
    # <===  r2l
    # ===>  l2r
    # ...
    
    toggle = True
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
      if toggle:
        levels.append(vals)
      else:
        levels.append(reversed(vals))
      toggle = not toggle
      curr_level = next_level
      next_level = []
    return levels  
    
