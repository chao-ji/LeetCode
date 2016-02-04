public class LC321
{
	public static void main(String[] args)
	{
	}

	// 321. Create Maximum Number
	static int[] maxNumber(int[] nums1, int[] nums2, int k)
	{
		int m = nums1.length;
		int n = nums2.length;
		int[] res = new int[k];

		for (int i = Math.max(0, k - n); i <= Math.min(k, m); i++)
		{
			int[] max1 = maxValue(nums1, i);
			int[] max2 = maxValue(nums2, k - i);
			int[] max = new int[k];
			int i1 = 0;
			int i2 = 0;
			int i3 = 0;
			while (max1.length > 0 && max2.length > 0 && i1 < max1.length && i2 < max2.length)
				if (isFirstLarger(max1, max2, i1, i2))
					max[i3++] = max1[i1++];
				else
					max[i3++] = max2[i2++];
			while (i1 < max1.length)
				max[i3++] = max1[i1++];
			while (i2 < max2.length)
				max[i3++] = max2[i2++];
			if (isFirstLarger(max, res, 0, 0))
				res = max;
		}
		return res;
	}

	static boolean isFirstLarger(int[] nums1, int[] nums2, int i, int j)
	{
		for (; i < nums1.length && j < nums2.length; i++, j++)
			if (nums1[i] > nums2[j])
				return true;
			else if (nums1[i] < nums2[j])
				return false;
		return i != nums1.length ? true : false;
	}

	static int[] maxValue(int[] nums, int k)
	{
		int[] max = new int[k];
		int len = nums.length;
		int j = -1;
		for (int i = 0; i < len; i++)
		{
			while (j >= 0 && max[j] < nums[i] && j + 1 + len - i > k)
				j--;
			if (j + 1 < k)
				max[++j] = nums[i];
		}	
		return max;
	}  
}
