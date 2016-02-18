public class LC4
{
	public static void main(String[] args)
	{
	}

	// 4. Median of Two Sorted Arrays
	static double findMedianSortedArrays(int[] nums1, int[] nums2)
	{
		if ((nums1.length + nums2.length) % 2 == 1)
			return (double) findK(nums1, nums2, (nums1.length + nums2.length + 1) / 2);
		else
			return (findK(nums1, nums2, (nums1.length + nums2.length) / 2) + findK(nums1, nums2, (nums1.length + nums2.length) / 2 + 1)) / 2.0;
	}

	static int findK(int[] nums1, int[] nums2, int k)
	{
		if (nums1.length == 0)
			return nums2[k - 1];
		else if (nums2.length == 0)
			return nums1[k - 1];

		int l = Math.max(k - nums2.length, 0);
		int h = Math.min(k, nums1.length);
		while (true)
		{
			int k1 = (l + h) / 2;
			int k2 = k - k1;

			int l1 = k1 >= 1 ? nums1[k1 - 1] : Integer.MIN_VALUE;
			int h2 = k2 <= nums2.length - 1 ? nums2[k2] : Integer.MAX_VALUE;
			int l2 = k2 >= 1 ? nums2[k2 - 1] : Integer.MIN_VALUE;
			int h1 = k1 <= nums1.length - 1 ? nums1[k1] : Integer.MAX_VALUE;

			if (l1 <= h2)
			{
				if (l2 <= h1)
					return Math.max(l1, l2);
				else
					l = k1 + 1;
			}
			else
				h = k1 - 1;
		}
	}
}
