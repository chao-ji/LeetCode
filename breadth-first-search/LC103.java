import java.util.*;

public class LC103
{
	public static void main(String[] args)
	{
	}

	// 103. Binary Tree Zigzag Level Order Traversal
	static List<List<Integer>> zigzagLevelOrder(TreeNode root)
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

		for (int i = 1; i < list.size(); i += 2)
			for (int j = 0; j < list.get(i).size() - 1 - j; j++)
			{
				int len = list.get(i).size();
				int save = list.get(i).get(j);
				list.get(i).set(j, list.get(i).get(len - 1 - j));
				list.get(i).set(len - 1 - j, save);
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
