"""24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # Nothing needs to be done if length of linked list <= 1
    if not head or not head.next:
      return head
    
    # Iterative approach. Can also be done using recursive approach. 
    # See LC 25 Reverse Nodes in k-Group
    
    # KEY Insight
    # Place a dummy node that precedes all nodes in the list.
    # Use two pointers `prev` and `curr`:
    
    # Initially we have:
    #
    # [] =====> [] =====> [] =====> some node or None
    # dummy     head      curr
    # prev      ^         ^
    #           |--swap---|
    
    # `prev.next` and `curr` points to two nodes to be swapped
    
    # `dummy.next` points to the start of the linked list to be swapped
    
    
    
    # To swap `prev.next` and `curr`:
    
    # 1. `next = curr.next`
    # [] =====> [] =====> [] =====> some node or None
    # prev      a         curr      next
    
    # 2. `curr.next = prev.next`
    # [] =====> [] =====> [],       some node or None
    # prev      a         curr      next
    #           ^          |
    #           |-----------      
    
    # 3. `prev.next.next = next`
    # [] =====> [] ===============> some node or None
    # prev      a                   next
    #           ^          
    #           |             []  
    #           ------------- curr
    
    # 4. `prev.next = curr`
    # [] =====> [] =====> [] =====> some node or None
    # prev      curr      a         next
    
    
    # `next` points to the start of the remaining linked list
    # that have not been swapped. We terminate the loop, If we
    # have <= 1 nodes in the remaining list:
      
    # ... ====> None
    #           next
    
    # or
    
    # ... =====> [] ====> None
    #            next
    
    # Initialize `prev` and `curr`
    prev = dummy = ListNode(0)
    dummy.next = head
    curr = prev.next.next
  
    # we proceed as long as the two nodes to be swapped, 
    # `prev.next` and `curr` are not empty.
    while prev.next and curr:
      # rewiring the connections
      next = curr.next
      curr.next = prev.next
      prev.next.next = next
      prev.next = curr
      
      # check if we need to terminate
      if not next or not next.next:
        break
      else:
        curr = next.next
        prev = prev.next.next
      
    return dummy.next  
