"""38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""
class Solution(object):
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    s = "1"
    # 1.     1
    # 2.     11
    # 3.     21
    # 4.     1211
    # 5.     111221 
    # 6.     312211
    # 7.     13112221
    # 8.     1113213211
    # 9.     31131211131221
    # 10.     13211311123113112211
    
    # Just Simulate the process of count and say:
    
    
    # Given `s` = 
    # d1, ..., d1, d2, ..., d2, ..., dn, ..., dn
    
    # `s` can be represented as a pattern [d1]*c1 [d2]*c2 [dn] * cn
    
    # which is exactly the count-n-say representation
    
    # where `d1` != `d2` != `dn`
    
    for i in range(2, n + 1):
      count = []
      value = []
      #
      for j in range(len(s)):
        # The first digit, or a different digit than the previous digit
        if not value or int(s[j]) != value[-1]:
          value.append(int(s[j]))
          count.append(1)
        # The same character as the one that precedes  
        elif int(s[j]) == value[-1]:
          count[-1] += 1
      s = ''.join([str(c) + str(v) for c, v in zip(count, value)])
    return s
