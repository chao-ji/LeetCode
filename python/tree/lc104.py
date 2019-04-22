"""104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # See LC 111, Minimum Depth of Binary Tree

    # Base case:
    # root is None, return 0
    if not root:
      return 0
    
    # We avoid making calls on empty trees (i.e. None)
    # and explicitly consider the four cases:
    
    # both subtrees are None, root is leaf
    if not root.left and not root.right:
      return 1
    # left is None, right is non-empty, recursive call on right subtree
    elif not root.left and root.right:
      return 1 + self.maxDepth(root.right)
    # right is None, left is non-empty, recursive call on left subtree
    elif root.left and not root.right:
      return 1 + self.maxDepth(root.left)
    # both subtrees are non-empty
    else:
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
