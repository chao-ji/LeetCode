public class LC101
{
	public static void main(String[] args)
	{
	}

	// 101. Symmetric Tree
	static boolean isSymmetric(TreeNode root)
	{
		if (root == null)
			return true;
		return isMirror(root.left, root.right);
	}

	static boolean isMirror(TreeNode root1, TreeNode root2)
	{
		if (root1 == null && root2 == null)
			return true;
		else if ((root1 == null && root2 != null) || (root1 != null && root2 == null))
			return false;
		return root1.val == root2.val && isMirror(root1.left, root2.right) && isMirror(root1.right, root2.left);    
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
