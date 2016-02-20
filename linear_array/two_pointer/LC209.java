public class LC209
{
	public static void main(String[] args)
	{
	}

	// 209. Minimum Size Subarray Sum
  static int minSubArrayLen(int s, int[] nums)
	{
		int l = 0;
		int h = 0;
		int sum = 0;

		while (h < nums.length)
		{
			sum += nums[h];
			if (sum >= s)
				break;
			h++;    
		}

		if (sum < s)
			return 0;

		while (sum - nums[l] >= s)
			sum -= nums[l++];

		int min = h - l + 1;
		h++;

		while (h < nums.length)
		{
			sum += nums[h];
			while (sum - nums[l] >= s)
				sum -= nums[l++];
			min = Math.min(min, h - l + 1);
			h++;
		}

		return min;
	}
}
