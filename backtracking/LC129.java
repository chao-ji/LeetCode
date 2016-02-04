import java.util.*;

public class LC129
{
	public static void main(String[] args)
	{
	}

	// 129. Sum Root to Leaf Numbers
	static int sumNumbers(TreeNode root)
	{
		if (root == null)
			return 0;

		List<TreeNode> path = new ArrayList<TreeNode>();
		path.add(root);
		int[] sum = new int[1];
		int[] val = new int[1];
		val[0] = root.val;
		recursive(path, sum, val);
		return sum[0];
	}

	static void recursive(List<TreeNode> path, int[] sum, int[] val)
	{
		if (path.isEmpty())
			return ;
		TreeNode node = path.get(path.size() - 1);
		if (node.left == null && node.right == null)
		{
			sum[0] = sum[0] + val[0];
			path.remove(path.size() - 1);
			val[0] = (val[0] - node.val) / 10;
			return ;
		}

		if (node.left != null)
		{
			path.add(node.left);
			val[0] = val[0] * 10 + node.left.val;
			recursive(path, sum, val);
		}
		if (node.right != null)
		{
			path.add(node.right);
			val[0] = val[0] * 10 + node.right.val;
			recursive(path, sum, val);
		}
		path.remove(path.size() - 1);
		val[0] = (val[0] - node.val) / 10;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
