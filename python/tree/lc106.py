"""106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def buildTree(self, inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if len(inorder) == 0:
      return None
    
    # The idea: use RECURSION
    
    # The LAST node in the postorder sequence is always the root,
    # We find the node in the inorder sequence with the same value as root, 
    # so we know which nodes are in the left subtree and right subtree:  
    
    # inorder =   [9,   3,    15,   20,   7]
    #                   i     i+1
    # postorder = [9,   15,   7,    20,   3]
    #                   i                 
    
    # root = 3  
    # left_inorder = [9]              # inorder[:i]
    # left_postorder = [9]            # postorder[:i]
  
    # right_inorder = [15, 20, 7]     # inorder[i+1:]
    # right_postorder = [15, 7, 20]   # postorder[i:-1]
    
    root_val = postorder[-1]
    # find the index of the root in the inorder sequence
    index = 0
    for i in range(len(inorder)):
      if inorder[i] == root_val:
        index = i
        break
        
    # Build left and right subtree recursively        
    left = self.buildTree(inorder[:index], postorder[:index])
    right = self.buildTree(inorder[index + 1:], postorder[index: -1])
    
    root = TreeNode(root_val)
    root.left = left
    root.right = right
    return root
