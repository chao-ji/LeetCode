public class LC104
{
	public static void main(String[] args)
	{
	}

	// 104. Maximum Depth of Binary Tree
	static int maxDepth(TreeNode root)
	{
		if (root == null)
			return 0;
		return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
