"""101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Solution 1,
# Recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
      return True
    
    # The idea: Use recursion
    
    # Given a non-empty root, if either of its child is None, 
    # then we are done:
    
    # left is None,       right is None,          is symmetric  
    # left is not None,   right is None           not symmetric
    # left is None,       right is not None       not symmetric
    
    # At this point, both children are not None, we need to recursively test if
    
    #
    #                left_child                        right_child
    #                 /      \                          /        \
    #              l_left    l_right                 r_left      r_right
    #                ^          ^                       ^           ^
    #                |          |                       |           |
    #                |          ------is symmetric ?---->           |
    #                |                                              |
    #                -----------------is symmetric ?-----------------
    
    return self.isMirror(root.left, root.right)
    
  def isMirror(self, root1, root2):
    """Checks if root1 is mirror image of root2 (and vice versa.) 
    i.e. flip(root1) == root2 and flip(root2) == root1 
    """
    if root1 is None and root2 is None:
      return True
    elif (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
      return False
    
    return (root1.val == root2.val 
            and self.isMirror(root1.left, root2.right) 
            and self.isMirror(root2.left, root1.right))

# Solution 2
# Iterative

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
      return True
    
    # The idea: do level-order traversal
    
    # For each level in the level-order traversal
    # We use two pointers to scan in left-to-right and right-to-left directions
    
    # At any point if the two pointers are not compatible:
    #   1. one is None and the other is not None
    #   2. both are not None but they hold different values
    # we return False
    
    curr_level = [root]
    next_level = []
    
    while curr_level:
      # `node` and `r_node` can be either None or not None 
      for node, r_node in zip(curr_level, reversed(curr_level)):
        if node and not r_node:
          return False
        elif not node and r_node:
          return False
        if node and r_node and node.val != r_node.val:
          return False
        
        # if `node` is not None
        # add `node.left` and `node.right` to next level
        if node:
          next_level.append(node.left)
          next_level.append(node.right)
        
      curr_level = next_level
      next_level = []
        
    return True     
