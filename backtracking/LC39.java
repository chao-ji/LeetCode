import java.util.*;

public class LC39
{
	public static void main(String[] args)
	{
	}

	// 39. Combination Sum
	static List<List<Integer>> combinationSum(int[] candidates, int target)
	{
		Arrays.sort(candidates);
		return recursive(candidates, 0, target);
	}

	static List<List<Integer>> recursive(int[] candidates, int start, int target)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();

		if (target == 0)
		{
			list.add(new ArrayList<Integer>());
			return list;
		}

		for (int i = start; i < candidates.length; i++)
			if (candidates[i] <= target)
			{
				List<List<Integer>> sub = recursive(candidates, i, target - candidates[i]);
				for (int j = 0; j < sub.size(); j++)
				{
					List<Integer> combination = new ArrayList<Integer>();
					combination.add(candidates[i]);
					combination.addAll(sub.get(j));
					list.add(combination);
				}
			}
		return list;        
	}
}
