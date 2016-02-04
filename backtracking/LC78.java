import java.util.*;

public class LC78
{
	public static void main(String[] args)
	{
	}

	// 78. Subsets
	static List<List<Integer>> subsets(int[] nums)
	{
		Arrays.sort(nums);
		return subsets(nums, 0);
	}

	static List<List<Integer>> subsets(int[] nums, int start)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (start == nums.length)
		{
			list.add(new ArrayList<Integer>());
			return list;
		}

		List<List<Integer>> sub = subsets(nums, start + 1);

		for (int i = 0; i < sub.size(); i++)
		{
			List<Integer> p = new ArrayList<Integer>();
			p.add(nums[start]);
			p.addAll(sub.get(i));
			list.add(p);
			list.add(sub.get(i));
		}
		return list;
	}
}
