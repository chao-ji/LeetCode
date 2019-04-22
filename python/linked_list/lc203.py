"""203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    # See LC 86 Parition List
    
    # KEY Insight:
    #
    # Disconnect the head node from the remaining input list
    # one at a time, and add it to the growing list if 
    # its `.val` field != val
    
  
    curr = dummy = ListNode(0)

    # Initially we have
    #
    # []  ====> None
    # dummy
    # curr
    #
    # `dummy.next` always points to the start of the growing 
    # linked list. `curr` is always the LAST node of the growing list
    # Initially the growing linked list is empty.
    
    # input linked list:
    # 
    # [] ====> [] ====> ... ===> [] ====> None
    # head
    # node
    
    # `node` will be stepped one at a time, and
    # `node` points to the node that MAY be removed. 
    
    
    # When removing, take note of the next node of `node`, disconnect
    # `node` from the remaining of linked list
    
    # [] =======> ... ====> [] ========> [] ======> ....
    #                       ^
    # head                  node         node.next
    
    # [] =======> ... ====> [] ===>None, [] ======> ....
    #                                    next
    #                                    node
    node = head
    while node:
      # take note of `node.next`
      next = node.next
      
      # remove `node` and add to the growing linked list
      if node.val != val:
        # disconnect
        node.next = None
        # add to the growing list:
        curr.next = node
        curr = curr.next
      # move `node` to the next node  
      node = next
      
    return dummy.next  
