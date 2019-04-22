"""147. Insertion Sort List

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def insertionSortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
      return head
    
    # `dummy.next` and `prev.next` points to the start of a sorted list (
    # initially empty)
    prev = dummy = ListNode(0)
    

    # Initially we have
    #
    # sorted list: (empty initally)
    #
    #     [   ] ========> None
    #     dummy
    #     prev
    
    # `curr` points to the start of the remaining list (i.e. the nodes to
    # be inserted), initially `head`
    curr = head
    # input list:
    # 
    #     [   ] =========> [    ] ======> ... ======> [] ====> None
    #
    #     head
    #     curr
    
    
    
    
    # In each iteration we insert one node (i.e. node pointed to by 
    # `node`) at a time
    
    # To insert a node pointed to by `curr`, we step `prev` until
    # `prev.next.val` >= 'curr.val` or `prev.next` is None
    
    # We have
    # sorted list:
    # [  ] ==> [0  ] ===> ... ===>[2  ] ====>[5   ] ====> ... ===> [] ====> None
    #                                       
    # dummy                       prev    ^  prev.next 
    #                                     |
    #                                  insertion
    
    # And we have 
    #    [ ] ===> [ ] ===> ... ===> [3 ] ====>  ... ====> None
    #                                ^
    #     head                       |
    #                               curr
    
    # So `curr` should be interted between `prev` and `prev.next`
    
    
    
    while curr:
      # 1. take note of `curr.next` to set `curr.next` back to later 
      next = curr.next
            
      # 2. while loop steps `prev` until we find the place for insertion
      while prev.next and prev.next.val < curr.val:
        prev = prev.next
      
      # 3. do the insertion: insert `curr` between `prev` and `prev.next`
      curr.next = prev.next
      prev.next = curr
      
      # 4. reset `prev` to `dummy`
      prev = dummy
      # and `curr` points to the next node to be inserted
      curr = next
      
    return dummy.next
