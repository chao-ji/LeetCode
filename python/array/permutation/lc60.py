"""60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"
"""
class Solution(object):
  def getPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    f = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
      if i == 1:
        f[i] = 1
      else:
        f[i] = i * f[i - 1]

    # The idea:
    #
    # It's like finding the `k`'th number in a numeral system with variable base: 
    #
    # fact(n - 1), fact(n - 2), ..., fact(1)
        
    # n = 4
    # f(1)    f(2)    f(3)     
    # 1       2       6       
    
    #                 k = k - 1
    #   1 2 3 4       0       
    #   1 2 4 3       1   1 // 6 = 0, 1 // 2 = 0, 1 // 1 = 1, 0
    #   1 3 2 4       2
    #   1 3 4 2       3   
    #   1 4 2 3       4
    #   1 4 3 2       5     
    #   
    #   2 1 3 4       6
    #   2 1 4 3       7   
    #   2 3 1 4       8   8 // 6 = 1, 2 // 2 = 1, 0 // 1 = 0, 0
    #   2 3 4 1       9
    #   2 4 1 3       10
    #   2 4 3 1       11
    #
    #   3 1 2 4       12
    #   3 1 4 2       13
    #   3 2 1 4       14  
    #   3 2 4 1       15  15 // 6 = 2, 3 // 2 = 1, 1 // 1 = 1, 0 
    #   3 4 1 2       16
    #   3 4 2 1       17   
    #
    #   4 1 2 3       18
    #   4 1 3 2       19
    #   4 2 1 3       20
    #   4 2 3 1       21
    #   4 3 1 2       22  22 // 6 = 3, 4 // 2 = 2, 0 // 1 = 1, 0
    #   4 3 2 1       23
    
    # Example:
    #
    # we have digits = [1, 2, 3, 4]
    #
    # k = 15, the "most significant" digit is 15 // 6 = 2, i.e. the 2nd digit -- 3
    # then, subtracting 6 * 2 from 15, we get leftover 3, and we're left with digits = [1, 2, 4]
    #
    # next,
    # 3 // 2 = 1, i.e. the 1st digit -- 2,
    # then, subtracting 2 * 1 from 3, we get leftover 1, and we're left with digits = [1, 4]
    #
    # next,
    # 1 // 1 = 1, i.e. the 1st digit -- 4,
    # then, subtracting 1 * 1 from 1, we get leftover 0, and we're left with digits = [1]
    #
    # [1] will be the least significant digit
    #
    # ==> 3, 2, 4, 1
    
    digits = list(range(1, n + 1))
    k -= 1
    perm = []
    
    while n - 1 > 0:
      q = k // f[n - 1]
      perm.append(str(digits.pop(q)))
      k = k - q * f[n - 1]
      n -= 1
    perm.append(str(digits.pop()))
    return ''.join(perm)
