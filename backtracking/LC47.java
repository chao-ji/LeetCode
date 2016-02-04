import java.util.*;

public class LC47
{
	public static void main(String[] args)
	{
	}

	// Permutations II
	static List<List<Integer>> permuteUnique(int[] nums)
	{
		Arrays.sort(nums);
		return recursive(nums);
	}

	static List<List<Integer>> recursive(int[] nums)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (nums.length == 1)
		{
			list.add(new ArrayList<Integer>());
			list.get(0).add(nums[0]);
			return list;
		}

		for (int i = 0; i < nums.length; i++)
		{
			if (i > 0 && nums[i] == nums[i - 1])
				continue;

			int[] a = new int[nums.length - 1];
			int k = 0;
			for (int j = 0; j < nums.length; j++)
				if (j != i)
					a[k++] = nums[j];

			List<List<Integer>> permutations = recursive(a);
			for (int j = 0; j < permutations.size(); j++)
			{
				List<Integer> p = new ArrayList<Integer>();
				p.add(nums[i]);
				p.addAll(permutations.get(j));
				list.add(p);
			}
		}

		return list;
	}
}
