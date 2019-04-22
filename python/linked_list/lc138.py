"""138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
  def copyRandomList(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head:
      return None

    # KEY Insight:
    # Use hash map to keep track of the mapping from the node in 
    # input list to the corresponding node in the new list.
    
    
    # If the `Node` instances had no `random` pointer, we only
    # need to scan the input linked list in one pass: 
    
    # Get two pointers `node_old` and `node_new` at the beginning
    # of the old and new linked list:
    # 1. create a new `Node` instance for the new list 
    # 2. step both `node_old` and `node_new`
    # 3. repeat 1 and 2
    
    # Initially we have 
    
    # input list:
    #
    # [] =====> [] =====> ... =====> []
    # head
    # node_old
    
    # new linked list:
    #
    # [] ======> None
    # dummy 
    # node_new
    
    # After some iterations we have
        
    # input list:
    #
    # [] =====> ... =====> [3] =====> [] ====> ...
    # head                           node_old
  
    # new linked list:
    #
    # [] ======> ... =====> [3] =====> None
    # dummy                 node_new
    
    # Note:
    # `node_old` points to the node to be copied
    # `node_new.next` points to the `Node` instance copied from `node_old` 
    
    
    
    
    
    
    # To handle the `random` pointers, we can use a HASH MAP that keeps
    # track of the mapping from the node in the INPUT LIST to node in 
    # the NEW LIST:
    #
    # And we need two passes:
    
    # The first pass is the same as the above -- pretend there were no
    # `random` pointers.
    
    # In the second pass, we need to set the `random` pointers for nodes
    # in the new list:
    
    # Whenever `node_old.random` is not None, it must point to a node
    # in the input list:
    
    # input list: 
    #
    # [] ======> [a] ====> ... ======> [b] =======> ...
    #             ^                    node_old
    #             |                    |
    #             ----------------------
    #             ^
    #             node_old.random
    
    # new list:
    #
    # [] ======> [a]=====> ... ======> [b] ========>
    #                                  node_new
    #
    
    # since `node_new` corresponds to `node_old`
    # `node_new.random` should point to `map[node_old.random]` 
    
    
    
    # Initialization
    old2new = {}
    node_old = head
    
    # `dummy.next` always points to the start of the growing linked list
    # `node_new` always points to the last node of the growing linked list
    node_new = dummy = Node(0, None, None)
    
    # First pass
    while node_old:
      # create new `Node` instance 
      node_new.next = Node(node_old.val, None, None)
      node_new = node_new.next
      
      # map from old to new
      old2new[node_old] = node_new
      
      node_old = node_old.next
    
    node_old = head
    node_new = old2new[head]
    
    # Second pass
    while node_old:
      # add `random` pointer
      if node_old.random:
        node_new.random = old2new[node_old.random]
      
      node_old = node_old.next
      node_new = node_new.next
    
    return old2new[head]    
        
