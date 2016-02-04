public class LC112
{
	public static void main(String[] args)
	{
	}

	// 112. Path Sum
	static boolean hasPathSum(TreeNode root, int sum)
	{
		if (root == null)
			return false;
		else if (root.left == null && root.right == null)
			return sum == root.val;
		return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);    
	}

	static class TreeNode
	{
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
