"""98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Solution 1,
# Recursive, inorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # The idea: do a inorder traversal
    
    # We keep track of the last value in the inorder squence, and 
    # compare if it is < than the value of the current node
    
    prev_val = [-float('inf')]
    return self.inorder(root, prev_val)
  
  def inorder(self, root, prev_val):
    """Returns whether the tree rooted at `root` is a valid BST,
    
    Performs inorder traversal of the tree
    
    `prev_val[0]` is the last value inf the inorder sequence
    """
    # Base case: 
    # empty node is always valid
    if not root:
      return True
    
    left = self.inorder(root.left, prev_val)
    # current value must be strictly > the previous value
    if root.val <= prev_val[0]:
      return False
    prev_val[0] = root.val
    right = self.inorder(root.right, prev_val)
    
    # tree is valid only both left and right subtrees are valid, and the previous
    # value < `root.val`
    return left and right

# Solution 2, 
# Recursive, use the definition of BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
      return True
    
    # The idea: we use the definition of BST:
    
    # a binary tree is a BST, if for any node
    # 1. all nodes in its left subtree hold keys < the node's key
    # 2. all nodes in its right subtree hold kyes > the node's key
    # 3. both left and right subtrees are valid BSTs themselves
    
    # We recursively test every non-empty node `node` in the tree:
    
    # 1. If left subtree is non-empty, then test if it is a valid BST
    # 2. If right subtree is non-empty, then test if it is a valid BST
    # 3. Test if the maximum value in left subtree < `node.val`, and
    #     if the minimum value if the right subtree > `node.val`
    
    # In addition, we also need to return the minimum and maximum value of the 
    # tree rooted at `node`.
    
    return self.isValidBSTMinMax(root)[0]
      
  
  def isValidBSTMinMax(self, root):
    """
    Returns if the tree rooted at `root` is a valid BST,
    and the min and max value of the tree -- min value always <= max value
    """
    # We explicitly test the four cases:
      
    # left is not None  &     right is not None
    # left is not None  &     right is None
    # left is None      &     right is not None
    # left is None      &     right is None

    # we avoid calling the function on empty nodes, so `root` is always non-empty.
      
    if root.left and root.right:
      left, left_min, left_max = self.isValidBSTMinMax(root.left)
      right, right_min, right_max = self.isValidBSTMinMax(root.right)
      return (left and right and left_max < root.val and root.val < right_min, 
             min(min(left_min, right_min), root.val), # min value 
             max(max(left_max, right_max), root.val)) # max value
    elif root.left and not root.right:
      left, left_min, left_max = self.isValidBSTMinMax(root.left)
      return left and left_max < root.val, min(left_min, root.val), max(left_max, root.val)
    elif not root.left and root.right:
      right, right_min, right_max = self.isValidBSTMinMax(root.right)
      return right and root.val < right_min, min(root.val, right_min), max(root.val, right_max)
    
    # Base case: `root` is leaf node
    return True, root.val, root.val   
