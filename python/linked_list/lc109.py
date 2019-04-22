"""109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    # KEY Insight:
    # Use two pointers where one moves twice as fast as the other
    # to find the mid point, 
    # then recursively build BST on both sides, and return BST rooted
    # at the midpoint, with the two BST as the left and right subtree.
    
    # Base case:
    # linked list has <= 1 node
    if not head:
      return None
    elif not head.next:
      return TreeNode(head.val)
    
    # two pointers that move at 1x and 2x speed
    p = q = head
    while p.next:
      p = p.next
      q = q.next
      if p.next:
        p = p.next
    
    # At this point, `p` points to the last node of the linked list, and
    # `q` points to the mid point:
    
    # [] ====> ... => []==> [] ==>[] ===> ... ======> []
    # head                  q                         p
    # <=====left=======>          <=======right========> 
    
    # Then we need to disconnect the left part from the remaining of
    # linked list:
    
    # move `node` from `head` until it points to the node before `q`:
    
    # [] ====> ... => []==> [] ==>[] ===> ... ======> []
    # head            node  q                         p
    # <=====left=======>          <=======right========> 
    
    node = head
    while node.next and node.next != q:
      node = node.next
      
    # disconenct the left part from the remaining of linked list  
    node.next = None
    
    # build left and right subtree recursively
    left = self.sortedListToBST(head)
    right = self.sortedListToBST(q.next)
    
    root = TreeNode(q.val)
    
    root.left = left
    root.right = right
    return root
