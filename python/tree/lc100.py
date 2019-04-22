"""100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# Solution 1
# Recursive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    # The idea: use the definition of Same Tree
    
    # Base case:
    if p is None and q is None:
      return True
    # One is non-empty, while the other is empty, then they are not the same
    elif (p is not None and q is None) or (p is None and q is not None):
      return False
    
    # Recursion step:
    # the root nodes of both trees must hold the Same Value,
    # and recursively test if 
    #   1. their left subtrees are the same
    #   2. their right subtrees are the same
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Solution 2
# Iterative, inorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """  
    # The idea: do level-order traversal
  
    # check the two sequences of nodes generated from level-order traversal
    # they must agree with each other (i.e. both are empty, or hold the same value)
    curr_level = [(p, q)]
    next_level = []
    
    while curr_level:
      # `p` can be either empty or non-empty
      # `q` can be either empty or non-empty
      for p, q in curr_level:
        if not p and q:
          return False
        elif p and not q:
          return False
        elif p and q and p.val != q.val:
          return False
        
        # at this point `p` and `q` are both non-empty or empty
        # add to `next_level` if both are non-empty
        if p and q:
          next_level.append((p.left, q.left))
          next_level.append((p.right, q.right))
          
      curr_level = next_level
      next_level = []
          
    return True        
