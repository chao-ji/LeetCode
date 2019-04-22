"""19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # KEY Insight:
    
    # 1. Use two pointers, let one of them be ahead of the other `n` steps
    # 2. Place a dummy node that points to `head` to handle corner
    #  case where `n` is the length of the linked list, i.e. remove the 
    #  head of the linked list.
    
    p = q = dummy = ListNode(0)
    dummy.next = head
    
    # Initially we have
    
    # [] ====> [] ====> ... ====> []
    # dummy    head
    # p
    # q
    
    # Next we must move `p` first, and let it be ahead
    # of `q` exactly `n` steps, and move both pointers
    # until `p` is the last node of the linked list
    
    # [] ====> ... ===> [] ===> [] === > ... ===> [] ===> None
    #
    # dummy             q       q.next            p
    #                   <======= n+1 nodes ========>
    
    # Now `q.next` points to the node to be deleted.
    # Note `q` could be still at `dummy` if `n` is the
    # length of the linked list
    
    for _ in range(n):
      p = p.next
      
    while p.next:
      p = p.next
      q = q.next
      
    q.next = q.next.next
    return dummy.next
