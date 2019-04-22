"""110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # The idea:
    
    # By definition, a balanced tree is one where both left and right subtree
    # are height-balanced, and their height should not differ by more than 1.
    
    # So we need to find 
    # 1. the heights of both subtrees
    # 2. whether both subtrees themselves are height-balanced
    
    return self.isBalancedWithDepth(root)[0]
  
  def isBalancedWithDepth(self, root):
    """
    Returns 
    1. if tree rooted at `root` is height-balanced.
    2. the depth of this tree
    """
    # Base case:
    # root is None,
    # return True, and depth (0)
    if not root:
      return True, 0
    
    left, left_depth = self.isBalancedWithDepth(root.left)
    right, right_depth = self.isBalancedWithDepth(root.right)
    
    depth = max(left_depth, right_depth) + 1
    
    return left and right and abs(left_depth - right_depth) <= 1, depth
