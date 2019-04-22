"""226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
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
  def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """   
    # The idea:
    
    # A tree is inverted if we swap the left and right child of EVERY node
    
    if not root:
      return root
    
    # as opposed to the iterative solution, the recursion solution swaps
    # left and right from the lowest level up to the highest level:
    
    #       4         level 0
    #     /   \
    #    2     7      level 1
    #   / \   / \
    #  1   3 6   9    level 2

    #       4         level 0
    #     /   \
    #    2     7      level 1
    #   / \   / \
    #  3   1 9   6    level 2,  inverted   <=== start inverting from lowest level
    
    #       4         level 0
    #     /   \
    #    7     2      level 1,  inverted
    #   / \   / \
    #  3   1 9   6    level 2,  inverted   

    
    # recursively invert the left and right subtree
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)
    
    # at this point, the left and right subtree have been inverted.
    # all that is left to do is to swap the left and and right subtree
    
    root.left = right
    root.right = left
    
    return root

# Solution 2
# Iterative

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
      return None
    
    # The idea:
    
    # A tree is inverted if we swap the left and right child of EVERY node
    
    # We traverse the nodes iteratively in level-order fashion
    
    #       4         level 0
    #     /   \
    #    2     7      level 1
    #   / \   / \
    #  1   3 6   9    level 2
    
    #       4         level 0
    #     /   \
    #    7     2      level 1,  inverted
    #   / \   / \
    #  1   3 6   9    level 2     
    
    #       4         level 0
    #     /   \
    #    7     2      level 1,  inverted
    #   / \   / \
    #  3   1 9   6    level 2,  inverted         
    
    queue = [root]
    while queue:
      node = queue.pop(0)
      
      # swap left and right child
      swap = node.left
      node.left = node.right
      node.right = swap
      
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      
    return root  
