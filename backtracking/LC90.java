import java.util.*;

public class LC90
{
	public static void main(String[] args)
	{
	}

	// 90. Subsets II
	static List<List<Integer>> subsetsWithDup(int[] nums)
	{
		Arrays.sort(nums);
		return subsetsWithDup(nums, 0);
	}

	static List<List<Integer>> subsetsWithDup(int[] nums, int start)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (start == nums.length)
		{
			list.add(new ArrayList<Integer>());
			return list;
		}

		List<List<Integer>> sub = subsetsWithDup(nums, start + 1);
		int j = start + 1;
		for (; j < nums.length && nums[j] == nums[start]; j++) ;
		int dup = j - start - 1;

		for (int i = 0; i < sub.size(); i++)
		{
			list.add(sub.get(i));
			if (dup == 0 || (sub.get(i).size() >= dup && sub.get(i).get(dup - 1) == nums[start]))
			{
				List<Integer> p = new ArrayList<Integer>();
				p.add(nums[start]);
				p.addAll(sub.get(i));
				list.add(p);
			}
		}
		return list;
	}
}
