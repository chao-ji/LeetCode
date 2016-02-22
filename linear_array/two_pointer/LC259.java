import java.util.*;

public class LC259
{
	public static void main(String[] args)
	{
	}

	// 259. 3Sum Smaller
	static int threeSumSmaller(int[] nums, int target)
	{
		if (nums.length < 3)
			return 0;
		Arrays.sort(nums);
		int count = 0;
		for (int i = 0; i < nums.length - 2; i++)
		{
			int low = i + 1;
			int high = nums.length - 1;
			while (low < high)
			{
				if (nums[i] + nums[low] + nums[high] < target)
				{
					count += high - low;
					low++;
				}
				else
					high--;
			}
		}
		return count;
	}
}
