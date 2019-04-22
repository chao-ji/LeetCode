"""108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    # The idea: use Recursion
    
    # Since the array is sorted, we can split it into two halves where the nodes in
    # the first half are sorted and less than the nodes in the second half, which are
    # also sorted.
    
    # a0, a1, ..., am-1, am, am+1, ..., an-1 
    # <====left=======>      <=====right===>
    
    # We can recursively biuld the left subtree and right subtree, which are guaranteed
    # to be balanced, since their length difference by no more than 1
    
    if len(nums) == 0:
      return None
    
    l, h = 0, len(nums) - 1
    # mid point
    m = (l + h) // 2
    # mid point is the root
    root = TreeNode(nums[m])
    # recursively build left and right subtree
    left = self.sortedArrayToBST(nums[:m])
    right = self.sortedArrayToBST(nums[m + 1:])
    root.left = left
    root.right = right
    return root
