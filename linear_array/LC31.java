public class LC31
{
	public static void main(String[] args)
	{
	}

	// 31. Next Permutation
	static void nextPermutation(int[] nums)
	{
		int len = nums.length;
		int i = len - 1;
		for (; i > 0 && nums[i - 1] >= nums[i]; i--) ;
		reverse(nums, i, len - 1);

		if (i > 0)
		{
			int j = i;
			for (; j < len && nums[j] <= nums[i - 1]; j++) ;
			int save = nums[i - 1];
			nums[i - 1] = nums[j];
			nums[j] = save;
		}
	}

	static void reverse(int[] nums, int i, int j)
	{
		while (i < j)
		{
			int save = nums[i];
			nums[i] = nums[j];
			nums[j] = save;
			i++;
			j--;
		}
	}
}
