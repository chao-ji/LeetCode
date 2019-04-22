"""21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
      return l2
    elif not l2:
      return l1
    # See LC 148 merge sort list
  
    # `dummy.next` points to the start of a merged list (initially empty)
    #
    # `node` points the end of merged list (initially empty)
    
    
    # [] =======> [] =====> ... ====> [] ======> None
    # dummy                           node
    
    # [] ===> .... ===> [] ===> ... ===>[] ===> None
    #                   l1
    #
    # [] ===> .... ===> [] ===> ... ===>[] ===> None
    #                   l2    
    
    node = dummy = ListNode(0)
    
    while l1 and l2:
      # `l1` and `l2` points to the head of the two linked lists
      # We pick whichever is smaller, and step the corresponding pointer, `l1` or `l2`
      
      if l1.val < l2.val:
        node.next = l1
        l1 = l1.next
      else:
        node.next = l2
        l2 = l2.next
        
      # We always step `node`  
      node = node.next
    
    if l1:
      node.next = l1
    if l2:
      node.next = l2
      
    return dummy.next  
