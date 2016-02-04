public class LC110
{
	public static void main(String[] args)
	{
	}

	// 110. Balanced Binary Tree
	static boolean isBalanced(TreeNode root)
	{
		if (root == null)
			return true;
		return Math.abs(getDepth(root.left) - getDepth(root.right)) <=1 && isBalanced(root.left) && isBalanced(root.right);
	}

	static int getDepth(TreeNode root)
	{
		if (root == null)
			return 0;
		return 1 + Math.max(getDepth(root.left), getDepth(root.right));
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
