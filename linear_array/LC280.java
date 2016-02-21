public class LC280
{
	public static void main(String[] args)
	{
	}

	// 280. Wiggle Sort
	static void wiggleSort(int[] nums)
	{
		for (int i = 1; i < nums.length; i++)
			if ((i % 2 == 1 && nums[i - 1] > nums[i]) || (i % 2 == 0 && nums[i - 1] < nums[i]))
			{
				int hold = nums[i - 1];
				nums[i - 1] = nums[i];
				nums[i] = hold;
			}
	}
}
