"""114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    # Intuition: use RECURSION
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    
    # Base case:
    # root is empty, just return None
    if not root:
      return root

    
    # recursively call the function on left subtree and right subtree
        
    left = self.flatten(root.left)
    right = self.flatten(root.right)
    
    # we have
    
    # left = 2 
    #         \
    #          3
    #           \
    #           4
    
    # right = 5
    #          \
    #           6    
    
    # reset `root` 's left child to None
    root.left = None

        
    # Add `left` as `root` 's right child:
    
    #      1
    #       \
    #        2 
    #         \
    #          3
    #           \
    #           4
    root.right = left

    # Get the last node of the all-right path,
    node = root
    while node.right:
      node = node.right

    # and set its right child to `right`:  
    node.right = right
    
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    #          \
    #           6
    
    return root

