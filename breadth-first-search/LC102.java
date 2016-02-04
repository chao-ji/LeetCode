import java.util.*;

public class LC102
{
	public static void main(String[] args)
	{
	}

	// 102. Binary Tree Level Order Traversal
	static List<List<Integer>> levelOrder(TreeNode root)
	{
		List<List<Integer>> levelorder = new ArrayList<List<Integer>>();
		if (root == null)
			return levelorder;
		Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
		List<Integer> level = new ArrayList<Integer>();
		queue.addLast(root);
		int count = 1;

		while (!queue.isEmpty())
		{
			int hold = 0;
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
			levelorder.add(level);
			level = new ArrayList<Integer>();
			count = hold;
		}
		return levelorder;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
