import java.util.*;

public class LC95
{
	public static void main(String[] args)
	{
	}

	// 95. Unique Binary Search Trees II
	static List<TreeNode> generateTrees(int n)
	{
		if (n == 0)
			return new ArrayList<TreeNode>();
		return generateTrees(1, n);
	}
    
	static List<TreeNode> generateTrees(int start, int end)
	{
		List<TreeNode> list = new ArrayList<TreeNode>();
		if (start > end)
		{
			list.add(null);
			return list;
		}
        
		for (int i = start; i <= end; i++)
		{
			List<TreeNode> left = generateTrees(start, i - 1);
			List<TreeNode> right = generateTrees(i + 1, end);
			for (int j = 0; j < left.size(); j++)
				for (int k = 0; k < right.size(); k++)
				{
					TreeNode root = new TreeNode(i);
					root.left = left.get(j);
					root.right = right.get(k);
					list.add(root);
				}
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
