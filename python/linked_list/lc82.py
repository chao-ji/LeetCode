"""82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # KEY Insight:
    #
    # For each node `curr` in the input linked list, 
    
    # 1. We find the next strictly greater node `next`
    # 2. If that node is the immediate successor of `curr`,
    #       -we add `curr` to the growing list;
    #       -otherwise we skip to `next` 
    
    # Initially, we have
    
    # `dummy.next` points to the start of the growing list, initially empty.
    # `node` points to the last node of the growing list, initially empty.
    
    # [] =====> None 
    #
    # dummy
    # node
    
    # [] ======> ...
    #
    # head
    # curr
    
    # To determine if a node has duplicates or not, we use a second pointer
    # `next`, starting from each pointer `curr`, and we move `next` until
    # `next.val` > `curr.val`
    
    #                    <---duplicate nums----> 
    #
    # [] ====> ... ====> [2] ====> ... ====> [2] ====> [3]
    #                    curr                          next        
    #
   
    #                    <-----  skipped   ----> 
    # [] ====> ... ====> [2] ====> ... ====> [2] ====> [3]
    #                                                  next        
    #                                                  curr
    
    # If `next` is not `curr.next`, then we skip to `next`, as shown above.
    
    # Otherwise, we disconnect `curr` from the remaining list and add
    # to the growing list
    
    node = dummy = ListNode(0)
    curr = head
    
    while curr:
      next = curr.next
      while next and next.val == curr.val:
        next = next.next
      # At this point,
      # `next` is None, or `next.val` > `curr.val`
    
      # If `next` is the immediate successor of `curr`, then `curr`
      # must be unique, so we add it to the growing list
      if curr.next == next:
        
        # disconnect `curr` from the remaining list
        curr.next = None
        
        # add to growing list
        node.next = curr
        node = node.next
      
      # `curr` points to the start of the remaining list
      curr = next
        
    return dummy.next
