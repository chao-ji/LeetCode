"""146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
class LRUCache(object):
  """
  Maintains a double-linked list, where each node stores the key and value of an item,
  and has two pointers `head` and `tail` which points to the previous neighbor and the 
  next neighbor in the list, `self.head` and `self.tail` points to the head and tail 
  node of the entire list, respectively.
  
  The head node of the list always stores the Least Recently Used (LRU) item, whereas
  the tail node of the list always stores the Most Recently Used item. Whenever a node
  is visited (`get` or `put'), we move it to the tail of the list.
  

                LRU                           MRU
                self.head                     self.tail
  
                node_1 <=> node_2 <=> ... <=> node_n
                
  hash   keys:  1          2                  n      
  """
  def __init__(self, capacity):
    """
    :type capacity: int
    """
    # max num of keys
    self.capacity = capacity
    # `hash` maps key to a node in the double-linked list
    self.hash = {}
    # pointers to the head and tail of the double-linked list
    self.head, self.tail = None, None
    
  def get(self, key):
    """
    :type key: int
    :rtype: int    
    """
    if key not in self.hash:
      return -1
    
    self._move_to_tail(self.hash[key])
    return self.hash[key].val
        
  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: None
    """
    # the item with key `key` is already present, just update its value,
    # and move it to the tail of the list    
    if key in self.hash:
      self._move_to_tail(self.hash[key])
      self.hash[key].val = value
      
    # Must create a new node `node`, and insert it into the list  
    else:
      node = Node(key, value)

      # Case1: We still have space to insert new item without having to remove the LRU.
      #
      # Just add it to the tail of the list
      if len(self.hash) < self.capacity:
        if len(self.hash) == 0:
          self.head = node
        else:
          # add `node` to the tail of list
          self.tail.tail = node
          node.head = self.tail  
      # Case2: We have reached the capacity, so we need to remove the LRU item (i.e. head) 
      # before a new one can be inserted.
      #
      # Delete the LRU (i.e. head), and add the node to the tail of the list
      elif len(self.hash) > 0:
        # delete the LRU element, i.e. `self.head`
        del self.hash[self.head.key]        

        # add `node` to the tail of list
        self.tail.tail = node    
        self.head = self.head.tail
        self.head.head = None  
        node.head = self.tail
        
      self.hash[key] = node  
      self.tail = node

  def _move_to_tail(self, node):
    """Move `node` in the double-linked list to the tail.
      
    If found, move `node_i` to the end (Most Recently Used)
    
    FROM
    
                LRU                                    MRU
                self.head                              self.tail
  
                node_1 <=> ... <=> node_i <=> ...  <=> node_n
                
         keys:  1                  i                   n          
    
    TO
    
                LRU                           MRU
                self.head                     self.tail
  
                node_1 <=> ... <=> node_n <=> node_i
                
         keys:  1                  n          i         
    Args:
      node: an Node instance, cannot be None.
    """
    # `node` is already the tail node of the list, nothing to do
    if not node.tail:
      return
    
    # Step1: splice `node` out of the list
    
    # `node` is the head node of the list
    if not node.head: 
      self.head = node.tail # move the head of the list to what was after the head
      node.tail.head = None
    # `node` is neither the head nor the tail of the list  
    else:
      node.head.tail = node.tail
      node.tail.head = node.head
    
    # Step2: add to the tail of the list
    self.tail.tail = node
    node.head = self.tail
    node.tail = None
    self.tail = node # move the tail of the list to newly added node
    
class Node(object):
  """Node of a double-linked list."""
  def __init__(self, key, val):
    self.head = None
    self.tail = None
    self.key = key
    self.val = val
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
