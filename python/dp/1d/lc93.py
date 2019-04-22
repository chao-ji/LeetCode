"""93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
class Solution(object):
  def restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s:
      return []
    
    # The idea: use dynamic programming
    
    
    #   <================= prefix ================>     <== suffix =>
    #   .     .     .     .     .     .     .     .     .     .     .
    #                                                   i-2         i
    #                                             j-1   <==== j ====>
    
    # Given string `s[:i+1]`, we look at the 
    
    # suffix `s[i]`
    # suffix `s[i-1]s[i]`
    # suffix `s[i-2]s[i-1]s[i]`
    
    # `i`: the ending index of the suffix, 
    # `j`: the starting index of the suffix, `j` = i - 2, i - 1, i    
    
    # `dp[i]` = the list of different ways of breaking s[:i+1] into <= 4
    # strings representing valid ip segment, i.e., 0 to 255
    
    # As long as the suffix `s[j:i + 1]` is valid, we look up the solution to
    # the subproblem `dp[j - 1]`, and extend each list of <= 3 valid ip segment
    # with the suffix `s[j:i+1]`, 
    
    # so `dp[i]` stores the different ways of breaking s[:i+1] into <= 4
    # valid ip segments.
    
    dp = []
    for i in range(len(s)):
      # `segments`: list of list of strings, 
      # the inner list has length <= 4
      segments = []
      for j in range(max(i - 2, 0), i + 1):
        if self.isValid(s[j:i + 1]):
          if j == 0:
            segments.append([s[j:i + 1]])
          elif dp[j - 1]:
            for segment in dp[j - 1]:
              if len(segment) <= 3:
                segments.append(segment + [s[j:i + 1]])

      dp.append(segments)
    return ['.'.join(segments) for segments in dp[-1] if len(segments) == 4]
      
  def isValid(self, ip_segment):      
    if len(ip_segment) == 1:
      return True
    elif len(ip_segment) == 2:
      return ip_segment[0] != '0'
    elif len(ip_segment) == 3:
      return ip_segment[0] != '0' and int(ip_segment) <= 255
      
    return False  
    
