"""83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
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
    
    # For this problem we won't use the dummy node approach.
    
    
    # We simply place one pointer `curr` at the head node, and maintain
    # the LOOP INVARIANT that the nodes between `head` and `curr`, inclusive,
    # are unique.
    
    # Initially, we have
    
    # []  ==== > .....
    # head
    # curr
    
    # In each iteration, we check if `curr` and `curr.next` have the same
    # value:
    
    # If `curr` and `curr.next` have different value, we simple step `curr`
        
    # [] ====> ... ====> [2] =====> [2] ======> [ ] =========> ...
    # head               curr       curr.next   curr.next.next
    
    # Otherwise, we splice `curr.next` out by setting `curr.next` to
    # `curr.next.next`
    
    # [] ====> ... ====> [2]        [2] ======> [ ] =========> ...
    # head               curr       curr.next   curr.next.next
    #                     |                      ^
    #                     |                      | 
    #                     ------------------------
    curr = head
    
    while curr and curr.next:
      # At the start of each iteration, 
      
      # 1. nodes from `head` up to `curr`, inclusive, contain nodes 
      # with unique values
      # 2. `curr.next` point to the start of the remaining linked list.
      
      
      # splice out `curr.next`
      if curr.next.val == curr.val:
        curr.next = curr.next.next
      # simply step `curr`  
      else:
        curr = curr.next
    return head    
