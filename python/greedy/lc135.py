"""135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""
class Solution(object):
  def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    # We have only three constraints:
    # 1. All children must be allocated >= 1 candy
    #
    # 2. left neighbor constraint:
    #    A child must have more candies than its left neighbor, if 
    #       ratings[i] > ratings[i - 1], for i in range(1, len(ratings))
    #
    # 3. right neighbor constraint:
    #    A child must have more candies than its right neighbor, if
    #       ratings[i] > ratings[i + 1], for i in range(0, len(ratings) - 1)
    #
    # Our GOAL is that at the end, we want all children in [1, len(ratings) - 2] 
    # to satisfy both the left neighbor and right neighbor constraints
    
    # We create `candies` to keep track of candy allocations
    #
    # All children must be allocated >= 1 candy
    candies = [1 for _ in range(len(ratings))]
    
    
    #
    #
    # At the beginning of each iteration, children 0, 1, ... i - 1
    # must satisfy the left neighbor constraint
    for i in range(1, len(ratings)):
      if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
        # increase `candies[i]` won't disrupt the left neighbor constraint
        # of those children to the left of `i`
        candies[i] = candies[i - 1] + 1
    
    # Up to this point, all of the `candies[i] = candies[i - 1] + 1` would be
    # necessary to satisfy the left neighbor constraints
        
    # At the beginning of each iteration, children i, i + 1, ..., len(ratings) - 1
    # must satisfy the right neighbor constraint,
    # 
    # In addition,
    # children 0, 1, i - 1
    for i in range(len(ratings) - 2, -1, -1):
      if (ratings[i] > ratings[i + 1] and 
          candies[i] <= candies[i + 1]): # checking `candies[i] <= candies[i + 1]`
                                         # makes sure that we increase `candies[i]`
                                         # only when necessary
        
        candies[i] = candies[i + 1] + 1
    
    return sum(candies)    
