"""105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    # The idea: use RECURSION
    
    # The FIRST node in the preorder sequence is always the root,
    # We find the node in the inorder sequence with the same value as root, 
    # so we know which nodes are in the left subtree and right subtree:
    
    # preorder =    [3,   9,    20,   15,   7]
    #                     i     i+1
    # inorder =     [9,   3,    15,   20,   7]
    #                     i     i+1
    
    # root = 3
    # left_preorder = [9]           #   preorder[1:i+1]
    # left_inorder = [9]            #   inorder[:i]
    
    # right_preorder = [20,15,7]    #   preorder[i+1:]
    # right_inorder = [15, 20, 7]   #   inorder[i+1:]
    

    # Base case: 
    # sequnce is empty, return empty tree
    if len(preorder) == 0:
      return None
    
    root_val = preorder[0]
    # find the index of the root in the inorder sequence
    index = 0
    for i in range(len(inorder)):
      if inorder[i] == root_val:
        index = i
        break
    
    # Build left and right subtree recursively
    left = self.buildTree(preorder[1:index + 1], inorder[:index])
    right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
    
    root = TreeNode(root_val)
    root.left = left
    root.right = right
    return root
