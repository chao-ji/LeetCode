import java.util.*;

public class LC107
{
	public static void main(String[] args)
	{
	}

	// 107. Binary Tree Level Order Traversal II
	static List<List<Integer>> levelOrderBottom(TreeNode root)
	{
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (root == null)
			return list;
		Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
		queue.addLast(root);
		int count = 1;
		while (!queue.isEmpty())
		{
			int hold = 0;
			List<Integer> level = new ArrayList<Integer>();
			for (int i = 0; i < count; i++)
			{
				TreeNode node = queue.removeFirst();
				level.add(node.val);
				if (node.left != null)
				{
					queue.addLast(node.left);
					hold++;
				}
				if (node.right != null)
				{
					queue.addLast(node.right);
					hold++;
				}
			}
			list.add(level);
			count = hold;
		}
		for (int i = 0; i < list.size() - 1 - i; i++)
		{
			int len = list.size();
			List<Integer> save = list.get(i);
			list.set(i, list.get(len - 1 - i));
			list.set(len - 1 - i, save);
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
