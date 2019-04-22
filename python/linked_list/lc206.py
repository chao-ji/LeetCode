"""206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, iterative
class Solution(object):
  def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # Nothing needs to be done for linked list with <= 1 nodes 
    if not head or not head.next:
      return head
    
    # At this point, linked list has at least two nodes:
    
    # Initially, we place three pointers `prev`, `curr`, `next`
    #
    # None      [   ]-------->[   ]-------->some node or None 
    #
    # prev      curr          next  
    
    # We maintain the following loop invariant:
    
    # At the beginning of each iterations,
    #
    # `curr` points to the node whose `.next` field is to be updated
    # `prev` points to the node that `curr`'s `.next` field should point
    #     to after the update
    # `next` points to the node immediately after `curr`
    
    
    # step1: curr.next = prev
    #
    #  None      [   ]--      [   ]------>some node or None
    #  ^ prev    curr  |      next
    #  |----------------
    
    # step2: prev = curr
    #
    #  None      [   ]--      [   ]------>some node or None
    #  ^         curr  |      next
    #  |         prev  |
    #  |----------------    
    
    # step3: curr = next
    #
    #  None      [   ]--      [   ]------>some node or None
    #  ^         prev  |      next
    #  |               |      curr
    #  |----------------        
    
    # step4: next = next.next
    #
    # None      [   ]---      [   ]------>some node or None
    #  ^         prev  |      curr        next
    #  |----------------
    #   
    prev = None
    curr = head
    next = head.next
    
    while next != None:
      curr.next = prev
      prev = curr
      curr = next
      next = next.next
      
    # At this point, `next` is None,
    # we point `curr.next` to the previous node `prev`
    # `curr` is node the head of the linked list
    curr.next = prev
    return curr
        
# Solution 2, recursive
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not head or not head.next:
      return head
    
    rev = self.reverseList(head.next)
    # disconnect `head` from the remaining of the linked list 
    
    # Now we have
    #
    # [   ]--->None     None<---[  ]<--- ... < ---[   ] 
    #
    # head                                        rev
    head.next = None
    
    
    # Get the last node of `rev` to point to `head`
    node = rev
    while node.next != None:
      node = node.next
    node.next = head
    
    return rev

