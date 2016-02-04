import java.util.*;

public class LC113
{
	public static void main(String[] args)
	{
	}

	// 113. Path Sum II
	static List<List<Integer>> pathSum(TreeNode root, int sum)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (root == null)
			return list;

		else if (root.left == null && root.right == null)
		{
			if (root.val == sum)
			{
				list.add(new ArrayList<Integer>());
				list.get(0).add(sum);
			}
			return list;
		}
		List<List<Integer>> left = pathSum(root.left, sum - root.val);
		List<List<Integer>> right = pathSum(root.right, sum - root.val);

		for (int i = 0; i < left.size(); i++)
		{
			List<Integer> path = new ArrayList<Integer>();
			path.add(root.val);
			path.addAll(left.get(i));
			list.add(path);
		}
		for (int i = 0; i < right.size(); i++)
		{
			List<Integer> path = new ArrayList<Integer>();
			path.add(root.val);
			path.addAll(right.get(i));
			list.add(path);
		}
		return list;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
