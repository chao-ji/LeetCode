"""133. Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:

      1 -- 2
      |    |
      3 -- 4


Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# Solution 1, BFS

class Solution(object):
  def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
      return None
    # The idea: BFS
    
    # use HASHMAP to link node in the old graph to the corresponding
    # node in the new graph
    
    # We can do a graph traversal to visit every node in the given graph exactly once 
    
    # We must do the following to copy the graph
    
    # 1. Create copies in the new graph for each node in the old graph
    # 2. Add edges between copies of nodes in the new graph.
    # 3. Establish mapping from nodes in old graph to their corresponding copies 
    #   in the new graph.
    
    
    # LOOP INVARIANT: 
    
    # For any node in the queue `queue`,
    # We must have already created their copies in the new graph, and
    # the old-to-new mapping have already been established.
    queue = [node]
    
    # This hashmap is also used to check if a node has been enqueued before for
    # Breadth First Search
    old2new = {node: Node(node.val, [])}
    
    # The follwing is just a modified BFS:
    while queue:
      # dequeue:
      p = queue.pop(0) 
      
      # Traverse `p`'s edges
      for n in p.neighbors:
        # check if node `n` has been enqueued before
        if n not in old2new:
          # As we enqueue node `n`, we also created its copy and add the 
          # old-to-new mapping, to maintain the LOOP INVARIANT
          queue.append(n)
          old2new[n] = Node(n.val, [])
        
        
        # node `p` is only dequeued ONCE, so we will only traverse `p`'s edges
        # exactly ONCE
        
        # By LOOP INVARIANT, `p` has already been enqueued, so its copy would be
        # `old2new[p]`, and the copy of `n` must have already been created, by the
        # above three lines of code. The following addes the edge from `p` to `n`
        # in the old graph to their copies in the new graph 
      
        old2new[p].neighbors.append(old2new[n])  

    return old2new[node]  

# Solution 2, DFS

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
  def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
      return None
    
    # The idea: 

    # Same as Solution 1, but uses DFS

    stack = [node]
    old2new = {node: Node(node.val, [])}
    
    while stack:
      p = stack.pop()
      
      for n in p.neighbors:
        if n not in old2new:
          stack.append(n)
          old2new[n] = Node(n.val, [])
          
        old2new[p].neighbors.append(old2new[n])
        
    return old2new[node]
