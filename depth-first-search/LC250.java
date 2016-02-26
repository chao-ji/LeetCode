public class LC250
{
	public static void main(String[] args)
	{
	}

	// 250. Count Univalue Subtrees
	static boolean isUnivalTree(TreeNode root, int[] count)
	{
		if (root == null)
			return true;

		boolean left = isUnivalTree(root.left, count);
		boolean right = isUnivalTree(root.right, count);
		boolean unique = false;

		if (root.left == null && root.right == null)
		{
			count[0]++;
			unique = true;
		}
		else if (root.left != null && root.right == null)
		{
			if (left == true && root.left.val == root.val)
			{
				count[0]++;
				unique = true;
			}
		}
		else if (root.left == null && root.right != null)
		{
			if (right == true && root.right.val == root.val)
			{
				count[0]++;
				unique = true;
			}
		}
		else if (root.left.val == root.val && root.right.val == root.val)
		{
			if (left == true && right == true)
			{
				count[0]++;
				unique = true;
			}
		}
		return unique;
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
