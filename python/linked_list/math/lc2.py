"""2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Same algorithm as LC 67 Add Binary
    
    # `curr` points to the current node of the result linked list
    curr = None
    # `bit_sum` is the running variable, storing the digit value of the sum (may
    #   have carryover from previous digit sums). Initialized to 0.
    bit_sum = 0
    while l1 or l2:
      # The iteration continues as long as we have at least one remaining digit
      # to be added, i.e. `l1` is not None and `l2` is not None
      if l1:
        bit_sum += l1.val
        l1 = l1.next
      if l2:
        bit_sum += l2.val
        l2 = l2.next

      # current digit value  
      if curr:
        # result linked list is not empty
        curr.next = ListNode(bit_sum % 10) 
        curr = curr.next
      else:
        # `curr` is the FIRST node
        curr = ListNode(bit_sum % 10) 
        head = curr
      # next digit value  
      bit_sum = bit_sum / 10
      
    # Don't forget the leading non-zero digit value  
    if bit_sum > 0:
      curr.next = ListNode(bit_sum % 10)
      curr = curr.next
    return head

