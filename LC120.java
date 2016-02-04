import java.util.*;

public class LC120
{
	public static void main(String[] args)
	{
	}

	// 120. Triangle
	static int minimumTotal(List<List<Integer>> triangle)
	{
		int len = triangle.size();
		int[] dp = new int[len];
        
		for (int i = len - 1; i >= 0; i--)
			if (i == len - 1)
				for (int j = 0; j < triangle.get(i).size(); j++)
					dp[j] = triangle.get(i).get(j);
			else
				for (int j = 0; j < triangle.get(i).size(); j++)
					dp[j] = Math.min(dp[j], dp[j + 1]) + triangle.get(i).get(j);
        
		return dp[0];
	}
}
