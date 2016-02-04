public class LC303
{
	public static void main(String[] args)
	{
	}

	// 303. Range Sum Query - Immutable
	static class NumArray
	{
		int[] cum;
		public NumArray(int[] nums)
		{
			int len = nums.length;
			cum = new int[len];
			for (int i = 0; i < len; i++)
				cum[i] = i == 0 ? nums[i] : nums[i] + cum[i - 1];
		}

		public int sumRange(int i, int j)
		{
			if (cum.length == 0)
				return 0;
			int val = i == 0 ? cum[j] : cum[j] - cum[i - 1];
			return val;
		}
	}
}
