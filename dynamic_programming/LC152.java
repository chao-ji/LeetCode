public class LC152
{
	public static void main(String[] args)
	{
	}

	// 152. Maximum Produt Subarray
	static int maxProduct(int[] nums)
	{
		int len = nums.length;
		int maxdp = nums[0];
		int mindp = nums[0];
		int prod = nums[0];
        
		for (int i = 1; i < len; i++)
		{
			if (nums[i] >= 0)
			{
				maxdp = maxdp > 0 ? maxdp * nums[i] : nums[i];
				mindp = mindp > 0 ? nums[i] : mindp * nums[i];
			}
			else
			{
				int max = mindp <= 0 ? mindp * nums[i] : nums[i];
				int min = maxdp <= 0 ? nums[i] : maxdp * nums[i];
                
				maxdp = max;
				mindp = min;
			}
			prod = prod < maxdp ? maxdp : prod;
		}
		return prod;
	}
}
